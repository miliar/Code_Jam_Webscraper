#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int getnextmov(vector<int> v);
void printVec(vector<char> v);
void printVec(vector<int> v);

int main()
{
    int loop1;
    vector<int> bvec;
    vector<int> ovec;
    vector<char> robot;
    vector<int> ans;
    char orange = 'O';
    char blue = 'B';
    ifstream in("A-large.in");
    in>>loop1;
    
    for(int i=0; i<loop1; i++)
    {
            int time = 1;
            bool seqfin = false;
            bool pushbutton = true;
            bool reacho = true;
            bool reachb = true;
            bool odone = false;
            bool bdone = false;
            char turn;
            int x=1;
            int y=1;
            int opos = 1;
            int bpos = 1;
            int loop2;
            in>>loop2;
            for(int j=0; j<loop2; j++)
            {
                 char robo;
                 in>>robo;
                 robot.push_back(robo);
                 if(robo == orange)
                 {
                      int mov;
                      in>>mov;
                      ovec.push_back(mov);
                 }
                 if(robo == blue)
                 {
                      int mov;
                      in>>mov;
                      bvec.push_back(mov);
                 }            
            }
            while(seqfin == false)
            {
                if(pushbutton == true)
                {
                     if(!robot.empty())
                     {         
                         turn = robot.front();
                         robot.erase(robot.begin());
                         //cout<<"Turn: "<<turn<<endl;
                     }
                     else
                     seqfin =true;
                     pushbutton = false;                         
                }
                 
                if(!ovec.empty()&&reacho==true)
                {
                    x = ovec.front();
                    //cout<<"x: "<<x<<endl;
                    ovec.erase(ovec.begin());
                    reacho = false;
                }
                
                if(!bvec.empty()&&reachb==true)
                {
                    y =  bvec.front();
                    //cout<<"y: "<<y<<endl;
                    bvec.erase(bvec.begin());
                    reachb =false;              
                }
                
                if(opos==x)
                {
                    if(turn == orange)
                    {
                        reacho = true;    
                        pushbutton = true;
                        //cout<<"orange push button"<<endl;         
                    }
                               
                }
                else
                {
                    if(opos<x)
                    {
                        opos++; 
                        //cout<<"orange position: "<<opos<<endl;         
                    }
                    if(opos>x)
                    {
                        opos--;
                        //cout<<"orange position: "<<opos<<endl;    
                    }    
                }
                
                if(bpos==y)
                {
                    if(turn == blue)
                    {
                        reachb = true;    
                        pushbutton = true;
                        //cout<<"blue push button"<<endl;         
                    }       
                }
                else
                {
                    if(bpos<y)
                    {
                        bpos++; 
                        //cout<<"blue position: "<<bpos<<endl;         
                    }
                    if(bpos>y)
                    {
                        bpos--;
                        //cout<<"blue position: "<<bpos<<endl;    
                    }    
                }
                
                if(ovec.empty()&&opos==x&&pushbutton==true)
                {
                    odone = true;                
                }
                if(bvec.empty()&&bpos==y)
                {
                    bdone = true;                
                }                
                if(odone==true&&bdone==true&&pushbutton==true&&robot.empty())
                {
                    break;                             
                }
                
                
                /*if(bvec.empty()&&ovec.empty()&&turn=='\0')
                {
                    seqfin = true;                              
                }*/
                time++;
                //cout<<"time: "<<time<<endl;
            }     
            //cout<<"the final time: "<<time<<endl<<endl<<endl;
            /*fstream t("output.txt");
            while(!t.eof())
            {
                char c;             
                t>>c;
                cout<<c;                 
            }
            t.seekp(ios::end);
            t<<"Case #"<<(i+1)<<": "<<time<<endl;
            t.close();*/
            ans.push_back(time);
                       
    }
    in.close();
    int f=1;
    fstream out("output.txt");
    while(!ans.empty())
    {
        out<<"Case #"<<f<<": "<<ans.front()<<endl;
        ans.erase(ans.begin());
        f++;    
    }
    out.close();
    //system("pause");
    return 0;    
}

int getnextmov(vector<int> &v)
{
    int mov = -1;
    if(!v.empty())
    {
          mov = v.front();
          v.erase(v.begin());
          return mov;            
    }    
    return mov;
}
void printVec(vector<char> v)
{
     vector<char>::iterator it;
     for(it=v.begin(); it<v.end(); it++)
     cout<<*it<<" ";     
}
void printVec(vector<int> v)
{
     vector<int>::iterator it;
     for(it=v.begin(); it<v.end(); it++)
     cout<<*it<<" ";     
}
