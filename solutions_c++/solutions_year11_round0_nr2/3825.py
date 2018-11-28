#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;


int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int C, D, N;
        cin >> C;
        string combine, oppose, invoke;
        if(C == 1)
            cin >> combine;
        cin >> D;
        if(D == 1) 
            cin >> oppose;
        int X; 
        cin >> X;
        cin >> invoke;
        string result;
        result += invoke[0];
        for(int i = 1; i < invoke.size(); i++)
        {
            if(C == 1 && result.size() > 0)
            if((invoke[i] == combine[0] && result[result.size() - 1] == combine[1]) || (invoke[i] == combine[1] && result[result.size() - 1] == combine[0]) )
            {
                result.erase(result.end() - 1);
		result += combine[2];
                continue;
            }
	    
	    if(D == 1 && result.size() > 0)
            if(invoke[i] == oppose[0])
	    {
		if(result.find(oppose[1], 0) != string::npos)
                {
			result = "";
                continue;
                }
	    }

	    if(D == 1 && result.size() > 0)
	    if(invoke[i] == oppose[1])
	    {
		if(result.find(oppose[0], 0) != string::npos)
                {
			result = "";
                continue;
                }
	    }
            result += invoke[i];
        }
        string answer;
        answer += "[";
        for(int i = 0; i < result.size(); i++)
            answer += result[i] + string(", ");
        if(result.size() > 0)
            answer.erase(answer.end() - 2, answer.end());
        answer += "]";
        printf("Case #%d: ", t);
        cout << answer << endl;
    }
    return 0;
}

