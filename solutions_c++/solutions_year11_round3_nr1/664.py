# include <iostream>
# include <vector>
# include <string>

using namespace std;

/*bool check (vector <string> grid,int row,int col)
{
     for (int i = 1;i < row;i++)
     {
         for (int j = 1;j < col;j++)
         {
             if (grid[i][j] == '#')
                return true;
         }
     }
     return false;
}*/               

/*bool replace (vector <string>& grid,int row,int col)
{
     for (int i = 1;i < row;i++)
     {
         for (int j = 1;j < col;j++)
         {
             int count = 0;
             if (grid[i][j] == '#')
             {
                  count = grid[i+1][j] != '#' ? count + 1 : count;
                  count = grid[i-1][j] != '#' ? count + 1 : count;
                  count = grid[i][j+1] != '#' ? count + 1 : count;
                  count = grid[i][j-1] != '#' ? count + 1 : count;
             }
             if (count      
         }
     }
     return false;
} */    
int main ()
{
    int test;
    cin>>test;
    for (int testid = 1; testid <=test;testid++)
    {
        int row,col;
        cin>>row>>col;
        vector <string> grid;
        string temp;
        for (int i=0;i < col + 2; i++)
        {
            temp.push_back ('.');
        }
        grid.push_back (temp);    
        for (int i=0;i< row;i++)
        {
            cin>>temp;
            temp = "." + temp + "."; 
            grid.push_back (temp);
        }
        temp.clear ();
        for (int i=0;i < col + 2; i++)
        {
            temp.push_back ('.');
        }
        grid.push_back (temp);
        bool flag =true;
        for (int i=1;i<row+1;i++)
        {
            int count = 0;
            for (int j=1;j<col+1;j++)
            {
                if (grid[i][j] == '#' && grid[i][j+1] == '#')
                {
                   grid[i][j] = '/';
                   grid[i][j+1] = '\\';
                }
                if (grid[i][j] == '#' && grid[i][j+1]!='#')
                   flag =false;  
            }
        }
        /*for (int i =1;i < (row + 1);i++)
        {
                for (int j=1;j < (col + 1);j++)
                {
                    cout<<grid[i][j];
                }
                cout<<endl;
        }*/
        for (int i=1;i<col+1;i++)
        {
            for (int j=1;j<(row+1);j++)
            {
                if (grid[j][i] =='/' && grid[j+1][i] == '/')
                {
                    //cout<<"Here"<<endl;
                    grid[j+1][i] = '\\';
                    j++;
                    continue;
                }
                if (grid[j][i] =='\\' && grid[j+1][i] == '\\')
                {
                    grid[j+1][i] = '/';
                    j++;
                    continue;
                }
                if (grid[j][i] =='\\' && grid[j+1][i] != '\\')
                {
                    //cout<<j<<i<<endl;
                    flag = false;
                }
                if (grid[j][i] =='/' && grid[j+1][i] != '/')
                {
                    //cout<<j<<i<<endl;
                    flag = false;
                }
            }
        }
        cout<<"Case #"<<testid<<":"<<endl;
        if (flag == false)                               
           cout<<"Impossible"<<endl;
        else
        {
            for (int i =1;i < row + 1;i++)
            {
                for (int j=1;j < col + 1;j++)
                {
                    cout<<grid[i][j];
                }
                cout<<endl;
            }
        }               
    }
    return 0;
}            
        
