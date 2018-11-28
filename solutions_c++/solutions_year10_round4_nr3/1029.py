#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int main()
{
    
    fstream input;
    string st;
    cin>>st;
    input.open(st.c_str(),ios::in);
    fstream output;
    output.open("output.txt",ios::out);
    int test;
    input>>test;
    for(int testno=1;testno<=test;testno++)
    {
            int n;
            input>>n;
            vector < vector <int> > v;
            for(int i=0;i<101;i++)
                    {
                     vector <int> temp(101);              
                                  v.push_back(temp);
                    }
            int minx,maxx,miny,maxy;
            minx = 10000;
            maxx = -1;
            miny = 10000;
            maxy = -1;
            for(int i=0;i<n;i++)
            {
                    int x1,x2,y1,y2;
                    input>>x1>>y1>>x2>>y2;
                   
                    if(minx>x1)
                               minx = x1;
                    if(maxx<x2)
                               maxx = x2;
                    if(miny>y1)
                               miny = y1;
                    if(maxy<y2)
                               maxy = y2;
                                      
                    for(int j=x1;j<=x2;j++)
                            for(int k=y1;k<=y2;k++)
                                    v[j][k] = 1;
                                    
            }   
            int iterations=0;
            int isiteration=1;
            while(isiteration)
            {
                              
                              isiteration=0;
               
            /*   for(int i=minx;i<=maxx;i++)
               {        for(int j=miny;j<=maxy;j++)
                               cout<<v[i][j];
                       cout<<endl;
               }
              */ 
                for(int i=maxx;i>=minx;i--)
                {
                        for(int j=maxy;j>=miny;j--)
                        {
                                if(v[i][j]==1)
                                {isiteration=1;
                                              if(v[i-1][j]==0&&v[i][j-1]==0)
                                                                            v[i][j]=0;
                                              
                                
                                }        
                                else
                                {
                                    if(v[i-1][j]==1&&v[i][j-1]==1)
                                    {                              v[i][j]=1;
                                                                  
                                    isiteration=1;
                                    }
                                }
                                
                        }        
                        
                        
                }
                if(isiteration==1)
                                  iterations++;
               // cout<<iterations<<endl;
                
            }
            
            output<<"Case #"<<testno<<": "<<iterations<<endl;
           
            
            
    }    
    output.close();
    input.close();
    system("pause");
    return 0;
    
}
