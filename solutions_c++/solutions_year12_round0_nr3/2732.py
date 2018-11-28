#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

/*
int main (int argc, char * const argv[]) 
{
	
	freopen("input2012_1.txt", "rt", stdin);
	freopen("output2012_1.txt", "wt", stdout);
	
//	string src = "abcdefghijklmnopqrstuvwxyz";
//	string tgt = "ynficwlbkuomxsevzpdrjgthaq";
    string tgth= "yhesocvxduiglbkrztnwjpfmaq";
    
    int T; 
	cin >> T;
	
	for(int i = 0; i <= T; i++) {
		string s;
		//cin >> s;
        getline(cin, s);
		
        if (i == 0)
            continue;
        
        cout << "Case #" << i << ": ";
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] >= 'a' && s[j] <= 'z')
            {
                cout << tgth[s[j]-'a'];
            }
            else
                cout << s[j];
            //cout << tgt[s[j] - 'a'];
        }
        cout << endl;
	}
    
	return 0;
}
*/
/*
int main (int argc, char * const argv[]) 
{
	freopen("input2012_2.txt", "rt", stdin);
	freopen("output2012_2.txt", "wt", stdout);
    
    int T; 
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		int N, S, p, t[100], flag[100];
		cin >> N;
        cin >> S;
        cin >> p;
        for (int j = 0; j < N; j++)
            cin >> t[j];
        
        // init flag
        for (int j = 0; j < N; j++)
            flag[j] = (j < S) ? 1 : 0;
        
        int maxover = 0, index = 0;
        while (1) {
            
            int overp = 0;
            for (int j = 0; j < N; j++) {
                int tm = t[j], tm3 = tm / 3;
                int max = 0;
                switch (tm % 3)
                {
                    case 0:
                        max = flag[j] == 1 ? tm3 + 1 : tm3;
                        if (tm == 0)
                            max = 0;
                        break;
                        
                    case 1:
                        max = tm3 + 1; 
                        break;
                        
                    case 2:
                        max = flag[j] == 1 ? tm3 + 2 : tm3 + 1;
                        if (tm3 + 2 > 10)
                            max = tm3 + 1;
                        break;
                        
                }
                if (max >= p)
                    overp++;
            }
            if (overp > maxover)
                maxover = overp;
            
            int found = 0;
            for (int j = 0; j < N - 1; j++) {
                if (flag[j] == 1 && flag[j+1] == 0) {
                    int s1 = 0;
                    for (int k = 0; k < j; k++) {
                        if (flag[k] == 1)
                            s1++;
                    }
                    for (int k = 0; k < j; k++)
                        flag[k] = (k < s1) ? 1 : 0;
                    flag[j] = 0;
                    flag[j+1] = 1;
                    found = 1;
                    break;
                }
            }
            if (found == 0)
                break;
            index++;
        }
        
        
        cout << "Case #" << i+1 << ": " << maxover << endl;
	}
    
	return 0;
}
*/
int main (int argc, char * const argv[]) 
{
	freopen("input2012_3.txt", "rt", stdin);
	freopen("output2012_3.txt", "wt", stdout);
    
    int T; 
	cin >> T;
	
    for(int i = 0; i < T; i++) {
        int A, B;
        cin >> A;
        cin >> B;
        
        int s = 0;
        int nd = 0, num = A;
        while (num > 0)
        {
            nd++;
            num /= 10;
        }
        
        for (int j = A + 1; j <= B; j++)
        {
            
            if (j < 10)
                continue;
            
            stringstream ss;
            ss << j;
            string sj = ss.str();
            
            
            int exist[6];
            for (int k = 0; k < 6; k++)
                exist[k] = 0;
            
            // k: digits of substr
            int e = 0;
            for (int k = nd - 1; k >= 1; k--) 
            {
                int l = nd - k;
                string sub;
                for (int m = 0; m < k; m++)
                    sub += sj[l + m];
                    
                string test = sub;
                for (int n = 0; n < l; n++)
                    test += sj[n];
                
                stringstream testss(test);
                int testn;
                testss >> testn;
                
                int found = 0;
                for (int n = 0; n < 6; n++)
                {
                    if (exist[n] == testn)
                    {
                        found = 1;
                        break;
                    }
                }
                if (found == 1)
                    continue;
                if (testn >= A && testn <= B && testn < j)
                {
                    exist[e++] = testn;
                    s++;
                }
            }
        }
        
        cout << "Case #" << i+1 << ": " << s << endl;

            
    }
    
	return 0;
}
