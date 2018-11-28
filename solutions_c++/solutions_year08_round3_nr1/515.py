#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
    long lf[1000];
    long kpl;
    int problem;
    int mul;
    int count;
    int perkey;
    long long total;
    int tc;
    int P;
    int L;
    int K;
    
    
    kpl = 0;
    
   	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    
    cin >> tc;
    //cout << tc << endl;
    //system("PAUSE");
    
    for(int i=1; i<=tc; i++)
    {
            problem = 0;
            
            cin >> P >> K >> L;
            for(int let=1; let<=L; let++)
            {
                    cin >> lf[let-1];
            }
            
            vector<int> myvector (lf, lf+L); 
            vector<int>::iterator it;
            
            sort(myvector.begin(), myvector.end());
            reverse(myvector.begin(),myvector.end());
            
            /*for(int let=1; let<=L; let++)
            {
                    cout << myvector[let-1];
            }*/
            
            mul = 1;
            count = 1;
            perkey = 0;
            
            for(int let=1; let<=L; let++)
            {
                    if(perkey > P)
                    {
                              problem = 1;
                              break;
                    }
                    myvector[let-1] *= mul;
                    if((count % K) == 0)
                    {
                             ++mul;
                             ++perkey;
                    }
                    ++count;
            }
            
            /*for(int let=1; let<=L; let++)
            {
                    cout << myvector[let-1];
            }*/ 
            
            if(!problem)
            {
                        total = 0;
                        
                        for(int j=1; j<=L; j++)
                        {
                                total += myvector[j-1];
                        }
                        
                        cout << "Case #" << i << ": " << total << endl;
            }
            else
            {
                        cout << "Case #" << i << ": Impossible" << endl;
            }

    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
