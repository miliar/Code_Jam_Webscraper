#include <iostream>
#include <vector>


const int MAX_BUTTONS=1000;

using namespace std;

//Orange == 0
//Blue == 1

int combination[30][30];
int bad_combination[30][30];
int my_set[30];

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests_count;
    cin >> tests_count;
    
    for (int test_num=0; test_num<tests_count; test_num++)
    {
        vector<char> answer;
        
        for (int i=0; i<30; i++)
            my_set[i]=0;
        
        for (int i=0; i<30; i++)
            for (int j=0; j<30; j++)
            {
                combination[i][j]=100;
                bad_combination[i][j]=0;
            }
        
        int comb_count;
        cin >> comb_count;
        
        for (int i=0; i<comb_count; i++)
        {
            string comb;
            cin >> comb;
            combination[(int)(comb[0]-'A')][(int)(comb[1]-'A')]=comb[2]-'A';
            combination[(int)(comb[1]-'A')][(int)(comb[0]-'A')]=comb[2]-'A';
        }
        
        int bad_comb_count;
        cin >> bad_comb_count;
        
        for (int i=0; i<bad_comb_count; i++)
        {
            string bad_comb;
            cin >> bad_comb;
            bad_combination[(int)(bad_comb[0]-'A')][(int)(bad_comb[1]-'A')]=1;
            bad_combination[(int)(bad_comb[1]-'A')][(int)(bad_comb[0]-'A')]=1;
        }
        
        int n;
        cin >> n;
        
        string s;
        cin >> s;
        
        int ss[1000];
        for (int i=0; i<n; i++)
            ss[i]=(int)(s[i]-'A');
        
        for (int i=0; i<n; )
        {
            if (i>0 && combination[ss[i]][ss[i-1]]<100)
            {
                ss[i-1]=combination[ss[i]][ss[i-1]];
                for (int j=i; j+1<n; j++)
                {
                    ss[j]=ss[j+1];
                }
                n--;
            }
            else
            {
                bool flag=false;
                for (int j=0; j<i; j++)
                    if (bad_combination[ss[j]][ss[i]])
                        flag=true;
                if (flag)
                {
                    for (int j=i+1; j<n; j++)
                        ss[j-i-1]=ss[j];
                    n=n-i-1;
                    i=0;
                }                
                else
                {
                    i++;
                }
            }
        }
        cout << "Case #" << test_num+1 << ": [";
        for (int i=0; i<n; i++)
        {
            cout << (char)(ss[i]+'A');
            if (i+1<n) cout << ", ";
        }
        cout << "]\n";
        
    }
    
    return 0;
}

