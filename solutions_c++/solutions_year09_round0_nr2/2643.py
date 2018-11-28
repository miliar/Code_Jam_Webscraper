#include <iostream>
#include <vector>

using namespace std;

void print_map(int w, int h, const vector<vector<int> > & map, bool numerically = true)
{
    for (int y = 0; y < h; ++y)
    {
        for (int x = 0; x < w; ++x)
        {
            if (numerically)
                cout << map.at(x).at(y) << " ";
            else
                cout << char('a' + map.at(x).at(y) - 1) << " ";
            
        }
        cout << endl;
    }
}

bool in_range(int w, int h, int x, int y)
{
    return x >= 0 && x < w && y >= 0 && y < h;
}

bool in_range_and_match(int w, int h, int x, int y, int off_x, int off_y, const vector<vector<int> > & map, int alt)
{
    return 
        in_range(w, h, x + off_x, y + off_y) && 
        map.at(x+off_x).at(y+off_y) == alt;
}

int find_lowest_neighbour_alt(int w, int h, int x, int y, const vector<vector<int> > & m)
{
    int l = 999999;
    
    if (in_range(w, h, x - 1, y) && m.at(x - 1).at(y) < l)
        l = m.at(x-1).at(y);
    
    if (in_range(w, h, x + 1, y) && m.at(x + 1).at(y) < l)
        l = m.at(x+1).at(y);
    
    if (in_range(w, h, x, y - 1) && m.at(x).at(y-1) < l)
        l = m.at(x).at(y-1);
    
    if (in_range(w, h, x, y + 1) && m.at(x).at(y+1) < l)
        l = m.at(x).at(y+1);
    
    return l;
}

void remark(int w, int h, vector<vector<int> > & marks, int old_mark, int new_mark)
{
    for (int y = 0; y < h; ++y)
        for (int x = 0; x < w; ++x)
            if (marks.at(x).at(y) == old_mark)
                marks.at(x).at(y) = new_mark;
}


void solve_map(int w, int h, const vector<vector<int> > & map)
{
    vector<vector<int> > marks(map);
    
    // Step 1: clear the marks
    for (int y = 0; y < h; ++y)
    {
        for (int x = 0; x < w; ++x)
        {
            marks.at(x).at(y) = 0;
        }
    }
    
    int n_marks = 0;
    // Step 2: mark cells that are connected as basin
    for (int y = 0; y < h; ++y)
    {
        for (int x = 0; x < w; ++x)
        {
            // find coordinates of the a lower cell or (0,0) if current is a sink
            int lowest_neighbour_alt = find_lowest_neighbour_alt(w, h, x, y, map);

            // if current is sink use new mark
            if (map.at(x).at(y) <= lowest_neighbour_alt)
            {
                if (marks.at(x).at(y) == 0)
                    marks.at(x).at(y) = ++n_marks;
            }
            else
            {
                // find coords of lower neightbour
                int nx, ny;
                
                if (in_range_and_match(w, h, x, y, 0, -1, map, lowest_neighbour_alt))
                {
                    nx = x;
                    ny = y - 1;
                }
                else
                    if (in_range_and_match(w, h, x, y, -1, 0, map, lowest_neighbour_alt))
                    {
                        nx = x - 1;
                        ny = y;
                    }
                else
                    if (in_range_and_match(w, h, x, y, +1, 0, map, lowest_neighbour_alt))
                    {
                        nx = x + 1;
                        ny = y;
                    }
                else
                    if (in_range_and_match(w, h, x, y, 0, +1, map, lowest_neighbour_alt))
                    {
                        nx = x;
                        ny = y + 1;
                    }
                else {
                    cout << "we have problem. line " << __LINE__ << endl;
                    exit(0);
                }
                
                int & current_mark = marks.at(x).at(y);
                int & neighbour_mark = marks.at(nx).at(ny);
                
                if (current_mark == 0 && neighbour_mark == 0)
                    current_mark = neighbour_mark = ++n_marks;
                else
                    if (current_mark == 0 && neighbour_mark != 0)
                        current_mark = neighbour_mark;
                else
                    if (current_mark != 0 && neighbour_mark == 0)
                        neighbour_mark = current_mark; 
                else
                    if (current_mark == neighbour_mark)
                    { /* nothing */}
                else
                    if (current_mark != neighbour_mark)
                        remark(w, h, marks, current_mark, neighbour_mark);
                else
                    {
                        cout << "we have problem. line " << __LINE__ << endl;
                        exit(0);
                    }
            }
        }
    }

    
    // print_map(w, h, marks);
    
    // step 3: labels from marks
    // negate the marks that means unlabeled 
    for (int y = 0; y < h; ++y)
        for (int x = 0; x < w; ++x)
            marks.at(x).at(y) = -marks.at(x).at(y);

    // scan the marks and label them sequentially
    int n_labels = 0;
    for (int y = 0; y < h; ++y)
        for (int x = 0; x < w; ++x)
        {
            if (marks.at(x).at(y) < 0)
                remark(w, h, marks, marks.at(x).at(y), ++n_labels);
        }
    
    if (n_labels > 26)
    {
        cout << "we have problem. line " << __LINE__ << endl;
        exit(0);
    }
    
    // cout << "Labeled:\n";
    print_map(w, h, marks, false);
}

int main()
{
    int n_maps;
    
    cin >> n_maps;
    
    for (int i_maps = 0; i_maps < n_maps; ++i_maps)
    {
        int h, w;
        
        cin >> h >> w;
        
        vector<vector<int> > map;
        
        for (int x = 0; x < w; ++x)
            map.push_back(vector<int>(h));
        
        for (int y = 0; y < h; ++y)
        {
            for (int x = 0; x < w; ++x)
            {
                cin >> map.at(x).at(y);
            }
        }
        
        cout << "Case #" << i_maps + 1 << ":" << endl;
        solve_map(w, h, map);
    }
}
