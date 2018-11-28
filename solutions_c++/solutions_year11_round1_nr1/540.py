#include<fstream>
using namespace std;
int main()
{
    ifstream in("A-large.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    long pd,pg;
    long long N;
    bool result[2001]={false};
    for(int i=0;i<T;i++)
    {
            in>>N>>pd>>pg;
            if((pg==100&&pd!=100)||(pg==0&&pd!=0))
            {
                                result[i]=false;
                                continue;
            }
            if(N>=100)
            {
                      result[i]=true;
                      continue;
            }
            else
            {
                for(int j=N;j>0;j--)
                if((j*pd)%100==0)
                {
                                 result[i]=true;
                                 break;
                }
            }
    }
    for(int i=0;i<T;i++)
    {
            out<<"Case #"<<i+1<<": ";
            if(result[i]==true)
            out<<"Possible";
            else
            out<<"Broken";
            out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
                
            
    
