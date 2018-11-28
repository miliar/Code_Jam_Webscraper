#include<iostream>
using namespace std;
char comb[1][3];
char opp[1][2];
char s[101];
int map[101];
int c, d, n;
void combine(int j);
int is_combined(int j);
void deleting();
int combine_num(int cur);
int main()
{
    //freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
    {
        cin >> c;
        for(int j=0; j<c; j++)
            for(int k=0; k<3; k++)
                cin >> comb[j][k];
        cin >> d;
        for(int j=0; j<d; j++)
            for(int k=0; k<2; k++)
                cin >> opp[j][k];
        cin >> n;
        for(int j=0; j<n; j++)
        {
            cin >> s[j];
            map[j] = 1;
        }
        deleting();
        cout << "Case #" <<i <<": [";
        int check = 0;
        for(int j=0; j<n; j++)
        {
            if(map[j])
            {
                if(check)
                    cout << ", ";
                cout << s[j];
                check = 1;
            }
        }
        cout <<"]"<< endl;
    }
}
void combine(int j)
{
    int next=-1;
    for(int k=j+1; k<n; k++)
        if(map[k])
        {
            next = k;
            break;
        }
    if(next!=-1)
    for(int k=0; k<c; k++)
    {
        if((s[j]==comb[k][0] && s[next] == comb[k][1])||(s[j]==comb[k][1] && s[next] == comb[k][0]))
        {
            map[next] = 0;
            s[j] = comb[k][2];
            break;
        }
    }
}
int is_combined(int j)
{
    int next=-1;
    for(int k=j+1; k<n; k++)
        if(map[k])
        {
            next = k;
            break;
        }
    if(next!=-1)
    {
        for(int k=0; k<c; k++)
        {
            if((s[j]==comb[k][0] && s[next] == comb[k][1])||(s[j]==comb[k][1] && s[next] == comb[k][0]))
            {
                return 1;
            }
        }
    }
    return 0;
}
void deleting()
{
    for(int i=0; i<n; i++)
    {
        if(map[i])
        {
            if(is_combined(i))
            {
                combine(i);
                continue;
            }
            int end = -1;
            for(int j=0; j<d; j++)
            {
                for(int k=0; k<2; k++)
                {
                    if(s[i]==opp[j][k])
                    {
                        for(int m = i+1; m<n; m++)
                        {
                            if(s[m]==opp[j][(k+1)%2] && combine_num(m)%2==0)
                            {
                                end = m;
                                break;
                            }
                        }
                    }
                    if(end!=-1)
                    {
                        for(int m=0; m<=end; m++)
                            map[m] =0;
                        break;
                    }
                }
                if(end!=-1)
                    break;
            }
        }
    }
}
int combine_num(int cur)
{
    int times =0;
    while((--cur)>=0 &&is_combined(cur))
    {
        times++;
    }
    return times;
}
