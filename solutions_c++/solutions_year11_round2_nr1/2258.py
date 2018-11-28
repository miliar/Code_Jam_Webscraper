#include<iostream>
using namespace std;

class AA{
    public:
        int win;
        int count;
        double wp;
        double owp;
        double oowp;
};

AA A[100];
char s[100][100];

int main(){
    int N;
    cin>>N;
   for(int i=1;i<=N;++i){
        int num;
        cin>>num;
        for(int j=0;j<num;++j){
            int count=0,win=0;
            for(int k=0;k<num;++k){
                char c;
                cin>>c;
                if(c=='1'){
                    ++count;
                    ++win;
                }
                if(c=='0')
                    ++count;
                s[j][k]=c;
            }
            A[j].win=win;
            A[j].count=count;
            A[j].wp=(double)win/count;
        }
        for(int j=0;j<num;++j){
            double total=0;
            for(int k=0;k<num;++k){
                if(s[j][k]=='.')
                    continue;
                if(A[k].count==1)
                    continue;
                total+=double(A[k].win-((s[j][k]=='1')?0:1))/(A[k].count-1);
            }
            A[j].owp=total/A[j].count;
        }

        for(int j=0;j<num;++j){
            double total=0;
            for(int k=0;k<num;++k){
                if(s[j][k]=='.')
                    continue;
                total+=A[k].owp;
            }
            A[j].oowp=total/A[j].count;
        }
        
        cout<<"Case #"<<i<<": "<<endl;
        for(int j=0;j<num;++j){
            cout<<A[j].wp*0.25+A[j].owp*0.5+A[j].oowp*0.25<<endl;
        }
    }
    return 0;
}
