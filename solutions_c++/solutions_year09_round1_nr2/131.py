#include<iostream>
using namespace std;

long t[50][50];
long s[20][20];
long w[20][20];
long st[20][20];

long C, c, M, N, i, j, tempt, temptempt;
int main()
{

    cin>>C;
    for(c=1;c<=C;c++)
    {
        cin>>N>>M;
        for(i=0; i<N; i++)
            for(j=0; j<M; j++)
            {
                cin>>s[i][j]>>w[i][j]>>st[i][j];
                
            }
        
        for(i=0; i< 2*N; i++)
            for(j=0; j<2*M; j++)
             {
                    
                        t[i][j] = -1;}
                
        t[2*N-1][0]=0;
        bool changed = true;
        cerr<<t[0][1];
        while(changed) {
                        changed = false;
                        cerr<<"reached "<<__LINE__<<endl;
        for(int diff=2*N-1; diff>= 1 - 2*M; diff--)
        {
            
            for(j=0; j<2*M; j++)
            {
                i = diff+j;
                if(i>=2*N)
                    break;
                    
                if(i<0)
                    continue;
                
                if(i%2 != 0 && j%2 == 0)
                {
                       cerr<<"reached "<<__LINE__<<endl;
                       bool done=false;
                       long tempt;
                       if( i!= 2*N - 1 )
                       {
                           tempt = t[i+1][j]+2;
                           done=true;
                       }
                       if( j!= 0 )
                       {
                           int temptempt = t[i][j-1]+2;
                           if(!done || temptempt < tempt)
                               tempt = temptempt;
                           done=true;
                       }
                       cerr<<tempt;
                       cerr<<"reached "<<__LINE__<<endl;
                       if( t[i-1][j]!= -1 )
                       {
                           int temptempt = t[i-1][j];
                           int stp = st[(i-1)/2][j/2];
                           int wp = w[(i-1)/2][j/2];
                           int sp = s[(i-1)/2][j/2];
                         
                            cerr<<"reached "<<__LINE__<<endl;
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;cerr<<"reached "<<__LINE__<<endl;                       cerr<<tempt;
                           if(temp >= sp )
                           {
                                   temptempt += sp+wp-temp+1;
                           }  
                           else
                           {
                               temptempt += 1;
                           }
                           if(!done || temptempt < tempt)
                             {    tempt = temptempt;done=true;}
                       }
                         cerr<<"reached "<<__LINE__<<endl;                       cerr<<tempt;
                       if( t[i][j+1] != -1 )
                       {
                           int temptempt = t[i][j+1];
                           int stp = st[(i-1)/2][j/2];
                           int wp = w[(i-1)/2][j/2];
                           int sp = s[(i-1)/2][j/2];
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += 1;
                           }
                           else
                           {
                               temptempt += sp - temp + 1;
                           }
                           if(!done || temptempt < tempt)
                           {    tempt = temptempt;done=true;}
                       }
                       
                       if(t[i][j]== -1 || tempt < t[i][j] )
                       {
                           changed = true;
                           t[i][j] = tempt;
                       }
                }
                
                else if( i%2 != 0 )
                {
                     
                     bool done=false;
                     long tempt;
                     if( i!= 2*N - 1 )
                     {
                         tempt = t[i+1][j]+2;
                           done=true;
                     }cerr<<done;
                     if( j!= 2*M - 1 && t[i][j+1]!= -1)
                     {
                         temptempt = t[i][j+1]+2;
                         if(!done || temptempt < tempt)
                             tempt = temptempt;
                         done=true;
                     }cerr<<done;
                     cerr<<t[i-1][j];
                     if(t[i-1][j] != -1 )
                     {
                         int temptempt = t[i-1][j];
                           int stp = st[(i-1)/2][j/2];
                           int wp = w[(i-1)/2][j/2];
                           int sp = s[(i-1)/2][j/2];
                        
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += sp+wp-temp+1;
                           }
                           else
                           {
                               temptempt += 1;
                           }
                           if(!done || temptempt < tempt)
                            {    tempt = temptempt;done=true;}
                     }cerr<<done;
                     if(t[i][j-1] != -1 )
                     {
                         cerr<<"reached "<<__LINE__;
                         int temptempt = t[i][j-1];
                           int stp = st[(i-1)/2][j/2];
                           int wp = w[(i-1)/2][j/2];
                           int sp = s[(i-1)/2][j/2];
                       
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           cerr<<temp;
                           if(temp >= sp )
                           {
                                   temptempt += 1;
                           }
                           else
                           {
                               temptempt += sp - temp + 1;
                           }
                           cerr<<temptempt;
                           if(!done || temptempt < tempt)
                           {    tempt = temptempt;done=true;}
                     }
                       if(t[i][j]== -1 || tempt < t[i][j] )
                       {
                           changed = true;
                           t[i][j] = tempt;
                       }
                }
                
                else if(j%2==0)
                {
                     bool done=false;
                     long tempt;
                     if( i!= 0 && t[i-1][j]!=-1)
                     {
                         tempt = t[i-1][j]+2;
                           done=true;
                     }
                     if( j!= 0 )
                     {
                         temptempt = t[i][j-1]+2;
                         if(!done || temptempt < tempt)
                             tempt = temptempt;
                         done=true;
                     }
                     if(t[i+1][j] != -1 )
                     {
                         int temptempt = t[i+1][j];
                           int stp = st[(i)/2][j/2];
                           int wp = w[(i)/2][j/2];
                           int sp = s[(i)/2][j/2];
                    
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += sp+wp-temp+1;
                           }
                           else
                           {
                               temptempt += 1;
                           }
                    
                           if(!done || temptempt < tempt)
                           {    tempt = temptempt;done=true;}
                     }
                     if(t[i][j+1] != -1 )
                     {
                         int temptempt = t[i][j+1];
                           int stp = st[(i)/2][j/2];
                           int wp = w[(i)/2][j/2];
                           int sp = s[(i)/2][j/2];
                    
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += 1;
                           }
                           else
                           {
                               temptempt += sp - temp + 1;
                           }
                           if(!done || temptempt < tempt)
                             {    tempt = temptempt;done=true;}
                     }
                     cerr<<tempt;
                     if(t[i][j]== -1 || tempt < t[i][j] )
                     {
                           changed = true;
                           t[i][j] = tempt;
                     }
                }
                else
                {
                     bool done=false;
                     long tempt;
                     if( i!= 0 && t[i-1][j]!=-1)
                     {
                         tempt = t[i-1][j]+2;
                           done=true;
                     }
                     if(j!= 2*M - 1 && t[i][j+1]!= -1)
                     {
                         temptempt = t[i][j+1]+2;
                         if(!done || temptempt < tempt)
                             tempt = temptempt;
                         done=true;
                     }
                     if(t[i+1][j] != -1 )
                     {
                         int temptempt = t[i+1][j];
                           int stp = st[(i)/2][j/2];
                           int wp = w[(i)/2][j/2];
                           int sp = s[(i)/2][j/2];
                   
                          
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += sp+wp-temp+1;
                           }
                           else
                           {
                               temptempt += 1;
                           }
                           if(!done || temptempt < tempt)
                             {    tempt = temptempt;done=true;}
                     }
                     if(t[i][j-1] != -1 )
                     {
                         int temptempt = t[i][j-1];
                           int stp = st[(i)/2][j/2];
                           int wp = w[(i)/2][j/2];
                           int sp = s[(i)/2][j/2];
                     
                           
                           int temp = (temptempt - stp)%(sp+wp);
                           if(temp < 0) temp += sp+wp;
                           if(temp >= sp )
                           {
                                   temptempt += 1;
                           }
                           else
                           {
                               temptempt += sp - temp + 1;
                           }
                           if(!done || temptempt < tempt)
                           {    tempt = temptempt;done=true;}
                     }
                     if(done && (t[i][j]== -1 || tempt < t[i][j] ))
                     {
                           changed = true;
                           t[i][j] = tempt;
                     }
                }
                cerr<<"t["<<i<<"]["<<j<<"] = "<< t[i][j] << endl;
            }
        }
        }
        
        cout<<"Case #"<<c<<": "<<t[0][2*M - 1]<<endl;
    }
}
        
                  
                     
