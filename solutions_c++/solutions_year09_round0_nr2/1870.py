#include <iostream> 
#include <fstream> 
#include <string>
#include <vector>   

using namespace std;

const char file_in[] = "B-large.in";
const char file_out[] = "B-large.out";


int T = 0;
bool sink = true;


struct Basins
{
    int H;
    int W;
};

struct Map
{
    int alt;
    char lable;
    bool islable;
    bool flag;
    Map *pmap;
    Map *rootmap;
};

int main()
{
    ofstream output; 
    ifstream input;
    Basins basins; 
    string test;

    input.open(file_in);
    output.open(file_out);
    if(input.fail())
    {
        cout<<"Open file error!"<<endl;
    }
    
    input>>T;

    for(int t=0; t<T; t++)
    {
        Map **map;
        int i = 0;
        int j = 0;
        sink = true;

        input>>basins.H>>basins.W;
        output<<"Case #"<<t+1<<":"<<endl;

        map = new Map*[basins.H];   
        for(i=0;i<basins.H;i++)
        {   
            map[i] = new Map[basins.W];   
        }

        for(i=0;i<basins.H;i++)
        {    
            for(j=0; j<basins.W; j++)
            {
                input>>map[i][j].alt;
                map[i][j].flag = false;
                map[i][j].islable = false;
                map[i][j].pmap = &map[i][j];
                map[i][j].rootmap = NULL;
                //cout<<map[i][j].alt<<" ";
            }
            //cout<<endl;
        }
        
        char lable = 'a';
        map[0][0].lable = lable; //first lable
        map[0][0].flag = true;
        map[0][0].islable = true;
        map[0][0].pmap = &map[0][0];
        int direction = 0;

        for(i=0; i<basins.H;i++)
        {    
            for(j=0; j<basins.W; j++)
            {
                sink = true;
                direction = 0;

                if(i>0)
                {
                    if(map[i][j].pmap->alt > map[i-1][j].alt)
                    {
                        map[i][j].pmap = &map[i-1][j];
                        map[i][j].flag = true;
                        direction = 1;
                    }
                    else if(map[i][j].alt == map[i-1][j].alt)
                    {
                        sink = false;
                    }
                }

                if(j>0)
                {
                    if(map[i][j].pmap->alt > map[i][j-1].alt)
                    {
                         map[i][j].pmap = &map[i][j-1];
                         map[i][j].flag = true;
                         direction = 2;
                    }
                    else if(map[i][j].alt == map[i][j-1].alt)
                    {
                        sink = false;
                    }
                }

                if((j+1)<basins.W)
                {
                    if(map[i][j].pmap->alt > map[i][j+1].alt)
                    {
                        map[i][j].pmap = &map[i][j+1];
                        map[i][j].flag = true;
                        direction = 3;
                    }
            
                    else if(map[i][j].alt == map[i][j+1].alt)
                    {
                        sink = false;
                    }                 
                }

                if((i+1)<basins.H)
                {
                   
                        if(map[i][j].pmap->alt > map[i+1][j].alt)
                        {
                            map[i][j].pmap = &map[i+1][j];
                            map[i][j].flag = true;
                            direction = 4;
                        }
                   
                        else if(map[i][j].alt == map[i+1][j].alt)
                        {
                            sink = false;
                        }
                    
                }
                
                if(map[i][j].flag)
                {

                    if(map[i][j].pmap != &map[i][j])
                        map[i][j].rootmap = map[i][j].pmap;
                }
            }
        }


            
        for(i=0; i<basins.H;i++)
        {    
            for(j=0; j<basins.W; j++)
            {    
                char templable = 0;
                Map *tempmap = NULL;
                Map *tempmap1 = NULL;
                bool tempflag = false;

                tempmap = &map[i][j];
                while(tempmap)
                {
                    if( (tempmap->islable) && (!tempflag) )
                    {
                        tempflag = true;
                        templable = tempmap->lable;
                    }
                    
                    if(tempflag)
                    {
                        tempmap->islable = true;
                        tempmap->lable = templable;
                    }

                    
                    tempmap1 = tempmap;
                    tempmap = tempmap->rootmap;

                   
                }

                if(!tempflag)
                {
                    tempmap1->islable = true;
                    tempmap1->lable = ++lable;
                }
                
                if(!map[i][j].islable)
                {
                    map[i][j].islable = true;
                    map[i][j].lable = tempmap1->lable;
                }                
            }
        }

        for(i=0; i<basins.H;i++)
        {    
            for(j=0; j<basins.W; j++)
            {
                
                //cout<<map[i][j].lable<<" ";
                output<<map[i][j].lable<<" ";
            }
            //cout<<endl;
            output<<endl;
        }

        //free
        for(i=0;i<basins.H;i++)
        {   
            delete[] map[i];   
        }

        delete[] map;
    }
    
    input.close();
    output.close();

    //system("PAUSE");
    return 0;
}
