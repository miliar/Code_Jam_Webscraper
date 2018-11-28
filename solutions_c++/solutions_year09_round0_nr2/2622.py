#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int lowest(int n, int w, int e, int s, int &val);
void adjust(vector<vector<char> > &basin, int H, int W, char smallch, char largech);

void display(vector<vector<char> > &basin, int H, int W)    
{
        return;
        for(int j=0; j<H; j++)
        {
            for(int k=0; k<W; k++)
            {
                clog << basin[j][k] << " ";
            }
            clog << endl;
        }        
        clog << endl;
        //system("PAUSE");
}

int main()
{
    int H;
    int W;
    int T;
    int i, j, k, x;
    char ch;
    char smallch, largech;
    int n, w, e, s, c;
    int low, val;
    
    ifstream infile;
    ofstream outfile;
    
    vector<vector<int> > map (100, vector<int> (100) );
    vector<vector<char> > basin (100, vector<char> (100, '.') );
    
    infile.open("watersheda.in");
    outfile.open("watersheda.out");
    
    infile >> T;
    for(i=0; i<T; i++)
    {
        infile >> H >> W;
        
        map.clear();
        map.resize(H);
        basin.clear();
        basin.resize(H);
        
        for(x=0; x<H; x++)
        {
            map[x].clear();
            map[x].resize(W);
            basin[x].clear();
            basin[x].resize(W);
        }
        
        for(j=0; j<H; j++)
            for(k=0; k<W; k++)
                infile >> map[j][k];
                
        for(j=0; j<H; j++)
            for(k=0; k<W; k++)
                basin[j][k] = '1';
                
        ch = 'a';                
        basin[0][0] = ch;
        
        //display(basin, H, W);
                        
        for(j=0; j<H; j++)
        {
            for(k=0; k<W; k++)
            {
                c = map[j][k];
                n = w = e = s = 11111;
                
                if((j-1) >= 0)
                    n = map[j-1][k];
                if((k-1) >= 0)
                    w = map[j][k-1];
                if((k+1) < W)
                    e = map[j][k+1];
                if((j+1) < H)
                    s = map[j+1][k];
                    
                low = lowest(n, w, e, s, val);
                
                basin[j][k] = (basin[j][k] == '1')?(++ch):basin[j][k];
                
                if(c > val)
                {
                    //basin[j][k] = (basin[j][k] == '1')?(++ch):basin[j][k];
                    
                    switch(low)
                    {
                        case 1: //n
                            basin[j-1][k] = (basin[j-1][k] == '1')?basin[j][k]:basin[j-1][k];
                            smallch = (basin[j-1][k] < basin[j][k])?basin[j-1][k]:basin[j][k];
                            largech = (basin[j-1][k] > basin[j][k])?basin[j-1][k]:basin[j][k];
                            if(smallch != largech)
                            {
                                adjust(basin, H, W, smallch, largech);
                                --ch;
                            }
                            break;
                        case 2: //w
                            basin[j][k-1] = (basin[j][k-1] == '1')?basin[j][k]:basin[j][k-1];
                            smallch = (basin[j][k-1] < basin[j][k])?basin[j][k-1]:basin[j][k];
                            largech = (basin[j][k-1] > basin[j][k])?basin[j][k-1]:basin[j][k];
                            if(smallch != largech)
                            {
                                adjust(basin, H, W, smallch, largech);                            
                                --ch;
                            }
                            break;
                        case 3: //e
                            basin[j][k+1] = (basin[j][k+1] == '1')?basin[j][k]:basin[j][k+1];
                            smallch = (basin[j][k+1] < basin[j][k])?basin[j][k+1]:basin[j][k];
                            largech = (basin[j][k+1] > basin[j][k])?basin[j][k+1]:basin[j][k];
                            if(smallch != largech)
                            {
                                adjust(basin, H, W, smallch, largech);                            
                                --ch;
                            }
                            break;
                        case 4: //s
                            basin[j+1][k] = (basin[j+1][k] == '1')?basin[j][k]:basin[j+1][k];
                            smallch = (basin[j+1][k] < basin[j][k])?basin[j+1][k]:basin[j][k];
                            largech = (basin[j+1][k] > basin[j][k])?basin[j+1][k]:basin[j][k];
                            if(smallch != largech)
                            {
                                adjust(basin, H, W, smallch, largech);
                                --ch;
                            }
                            break;
                    }
                }
                //clog << "after case..." << endl;
                //display(basin, H, W);                
            }
        }
        
        outfile << "Case #" << i+1 << ":" << endl;
        for(j=0; j<H; j++)
        {
            for(k=0; k<W; k++)
            {
                outfile << basin[j][k] << " ";
                //clog << basin[j][k] << " ";
            }
            outfile << endl;
            //clog << endl;
        }
        //system("PAUSE");
    }
    
    infile.close();
    outfile.close();
    return 0;
}

int lowest(int n, int w, int e, int s, int &val)
{
    int r1, r2, v1, v2;
    int r, v;
    
    r1 = n<=w?1:2;
    v1 = n<=w?n:w;
    r2 = e<=s?3:4;
    v2 = e<=s?e:s;
    
    r = v1<=v2?r1:r2;
    v = v1<=v2?v1:v2;
    
    val = v;
    return r;
}

void adjust(vector<vector<char> > &basin, int H, int W, char smallch, char largech)
{
    //display(basin, H, W);
    //clog << "adjusting..." << endl;
    for(int i=0; i<H; i++)
    {
        for(int j=0; j<W; j++)
        {
            basin[i][j] = (basin[i][j] == largech)?smallch:basin[i][j];
            basin[i][j] = (basin[i][j] > largech)?(basin[i][j]-1):basin[i][j];
            //clog << basin[i][j] << " ";
        }
        //clog << endl;
    }
    //clog << endl;
    //system("PAUSE");
}

                
