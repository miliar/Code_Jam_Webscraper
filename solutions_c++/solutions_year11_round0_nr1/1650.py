#include<fstream>
using namespace std;
int Abs(int a)
{
    if(a<0)
    return -a;
    else
    return a;
}
int main()
{
    ifstream in("A-large.in");
    ofstream out("out.txt");
    int T;
    char c,d=0;
    in>>T;
    int pos,Lpos=1;
    int N;//number of integers
    long result[101]={0};
    long sequ[101];
    int stB=0,stO=0;
    int posB=1,posO=1;
    int B[101]={0},O[101]={0};
    for(int i=0;i<T;i++)
    {
            in>>N;
            for(int j=1;j<=N;j++)
            {
                    in>>c;
                    in>>pos;
                    if(c==d)
                    {
                            result[i]+=Abs(pos-Lpos)+1;
                            if(c=='B')
                            {
                                      stO+=Abs(pos-Lpos)+1;
                                      posB=pos;
                            }
                            else
                            {
                                stB+=Abs(pos-Lpos)+1;
                                posO=pos;
                            }
                    }
                            
                    else
                    {
                        if(c=='B')
                        {
                                  if(stB>=Abs(pos-posB))
                                  {
                                                             result[i]+=1;
                                                             stO=1;
                                                             posB=pos;
                                  }
                                  else
                                  {
                                      result[i]+=Abs(pos-posB)-stB+1;
                                      stO=Abs(pos-posB)-stB+1;
                                      posB=pos;
                                  }
                        }
                        else
                        {
                             if(stO>=Abs(pos-posO))
                             {
                                                        result[i]+=1;
                                                        stB=1;
                                                        posO=pos;
                             }
                             else
                             {
                                      result[i]+=Abs(pos-posO)-stO+1;
                                      stB=Abs(pos-posO)-stO+1;
                                      posO=pos;
                             }
                        }
                    }
                    d=c;
                    Lpos=pos;
            }
            stB=0;
            stO=0;
            posB=1;
            posO=1;
            Lpos=1;
    }
    for(int i=0;i<T;i++)
    {
            out<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
    return 0;
}

                        
                    
                        
                    
                    
                    
            
            
