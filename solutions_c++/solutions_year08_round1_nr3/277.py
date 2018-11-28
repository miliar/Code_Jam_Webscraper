#include<string>
#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    string s[]={"001","005","027","143","751","935","607","903","991","335","047","943","471","055","447","463","991","095","607","263","151","855","527","743","351","135","407","903","791","135","647"};
    int N;
    cin>>N;
    int n;
    for(int i=0;i<N;i++)
    {
        cin>>n;
        cout<<"Case #"<<i+1<<": "<<s[n]<<endl;
    }
    return 0;
}
