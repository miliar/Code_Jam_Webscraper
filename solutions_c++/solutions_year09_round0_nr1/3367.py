#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int l,d,n;
    cin>>l>>d>>n;
    vector<string> v;
    string s;
    for(int i=0;i<d;i++)
    {
        cin>>s;
        v.push_back(s);
    }
    for(int i=0;i<n;i++)
    {
        cin>>s;
        int c=0;//count
        for(int q=0;q<d;q++)
        {
            int j=0;// s
            int k=0;// v[i]
            int r=1;//right word
            while(s[j]!='\0')
            {
                if(s[j]=='(')
                {
                    j++;
                    r=0;
                    while(s[j]!=')')
                    {
                        if(s[j]==v[q][k])
                        {
                            r=1;
                            k++;
                            break;
                        }
                        j++;
                    }
                    while(s[j]!=')') j++;
                    j++;
                    if(r==0) break;
                }
                else
                {
                    if(v[q][k]==s[j])
                    {
                        j++;
                        k++;
                    }
                    else
                    {
                        r=0;
                        break;
                    }
                }
            }
            if(r==1) c++;
        }
        cout<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0;
}
