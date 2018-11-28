#include<fstream>
#include<algorithm>
using namespace std;
ifstream fin("B.in");
ofstream fout("B.out");
int score[110],N,S,P;
int main()
{
    int T;
    fin>>T;
    for(int c=1;c<=T;c++)
    {
        fin>>N>>S>>P;
        //if(c==66)fout<<"-----"<<N<<" "<<S<<" "<<P<<" ";
        for(int i=0;i<N;i++)
        {
          fin>>score[i];
          //if(c==66)
          //fout<<score[i]<<" ";
        }
        //if(c==66)fout<<endl;
        int least;
        least=3*P-2;
        if(least<0)least=0;
        //fout<<least<<endl;
        sort(score,score+N);
        reverse(score,score+N);
        int suse=-1,res=0;
        if(P<=1)S=0;
        for(int i=0;i<N;i++)
        {
           if(score[i]>=least)res++;
           else
           {
             suse=i;
             break;
           }
        }
        if(suse!=-1&&S)
        {
            for(int i=0;i<S;i++)
            {
               if(score[suse]>=3*P-4)
               res++;
               else
               break;
               suse++;
            }
        }
        fout<<"Case #"<<c<<": "<<res<<endl;
    }
    return 0;
}
