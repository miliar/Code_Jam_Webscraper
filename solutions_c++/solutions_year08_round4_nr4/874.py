#include <iostream>
#include <vector>
using namespace std;
int RLE(string str)
{
        int k=0;
        char l=' ';
        for(int i=0;i<str.length();i++)
                if(str[i]!=l)
                {
                        l=str[i];
                        k++;
                }
        return k;
}
int code(string st,vector<int>per)
{
        string str;
        for(int i=0;i<st.length()/per.size();i++)
                for(int j=0;j<per.size();j++)
                        str+=st[i*per.size()+per[j]];
        return RLE(str);
}
int main()
{
        int n;
        string s;
        vector<int>v;
        cin>>n;
        for(int cn=1;cn<=n;cn++)
        {
                int mi,k;
                mi=999;
                cin>>k>>s;
                v.clear();
                for(int i=0;i<k;i++)
                     v.push_back(i);
                do
                        mi=min(mi,code(s,v));
                while(next_permutation(v.begin(),v.end()));
                printf("Case #%d: %d\n",cn,mi);
        }
        return 0;
}
