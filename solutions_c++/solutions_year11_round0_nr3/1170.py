#include<iostream>
using namespace std;
char comb[100][3];
char opp[100][2];
char s[101];
int map[101];
int c, d, n;
void combine(int j);
int is_combined(int j);
void deleting();
int combine_num(int cur);
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1;i<=t;++i)
    {
        int n;
        long min = 9999999;
        long sum = 0;
        long temp;
        long now=0;
        cin>>n;
        for(int j = 0;j!=n;++j)
        {
            cin>>temp;
            sum+=temp;
            if(temp<min) min = temp;
            now^=temp;
        }
        if(now != 0)
        {
            cout<<"Case #"<<i<<": NO"<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<sum - min<<endl;
        }
    }
}

