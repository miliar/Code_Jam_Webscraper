#include<fstream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

int main()
{
    int T,I,C,D,N,i,j,k;
    vector<char> str;
    char ch;
    vector<vector<char> > combine,opposed;
    cin>>T;
    for(I=1;I<=T;I++)
    {
        cin>>C;
        combine.resize(C);
        for(i=0;i<C;i++)
        {
            combine[i].resize(3);
            cin>>combine[i][0]>>combine[i][1]>>combine[i][2];
        }
        cin>>D;
        opposed.resize(D);
        for(i=0;i<D;i++)
        {
            opposed[i].resize(2);
            cin>>opposed[i][0]>>opposed[i][1];
        }
        cin>>N;
        for(i=0;i<N;i++)
        {
            cin>>ch;
            str.push_back(ch);
            if(str.size()==1)continue;
            for(j=0;j<C;j++)
            {
                if( (*(str.end()-1)==combine[j][0] && *(str.end()-2)==combine[j][1])  ||
                    (*(str.end()-1)==combine[j][1] && *(str.end()-2)==combine[j][0])  )
                {
                    str.erase(str.end()-2,str.end());
                    str.push_back(combine[j][2]);
                }
            }
            for(j=0;j<D;j++)
            {
                for(k=0;k<str.size();k++)
                {
                    if((str[k]==opposed[j][0] && str[str.size()-1]==opposed[j][1])    ||
                       (str[k]==opposed[j][1] && str[str.size()-1]==opposed[j][0]))
                    {
                        str.clear();
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<I<<": [";
        for(i=0;i<int(str.size())-1;i++)
            cout<<str[i]<<", ";
        if(!str.empty())
            cout<<str[str.size()-1];
        cout<<"]"<<endl;
        str.clear();
    }
    return 0;
}
