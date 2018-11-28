#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <sstream>
#include <map>
#include <set>
using namespace std;

map<pair<int, int>, string> dict;

string int2str(int val, int base)
{
    string ret("");
    while(val){
	ret = (char)('0' + val % base) + ret;
	val /= base;
    }
    return ret;
}

int str2int(const string& ss)
{
    int j, ret;
    for(j = 0, ret = 0; j < ss.size(); j++)
	ret += (ss[j] - '0') * (ss[j] - '0');
    return ret;
}

bool judge(int val, int base)
{
    string ss = int2str(val, base);    
    int next;
    bool vis[100001];
    memset(vis, false, sizeof(vis));
    vis[val] = true;
    while(true){	
	next = str2int(ss);	
	//cout<<ss<<" "<<next<<endl;
	if(vis[next])
	    return false;
	vis[next] = true;
	if(next == 1)
	    return true;
	ss = int2str(next, base);		
    }
    return false;
}

int main()
{
    int tt, j, k, l, base[10], cnt, bb;
    char ss[1024];
    //scanf("%d", &tt);
    //getchar();
    //judge(82, 10);
    //judge(143, 2);
    //judge(143, 3);
    scanf("%d", &tt);
    getchar();
    for(j = 1; j <= tt; j++){
	memset(ss, 0, sizeof(ss));
	gets(ss);
	stringstream str(ss);
	cnt = 0;
	while(str>>bb){
	    base[cnt++] = bb;
	}
	//for(k = 0; k < cnt; k++)
	    //printf("%d ", base[k]);
	//printf("\n");
	k = 2;
	bool flag = true;
	for(k = 2; k <= 100000; k++){
	    for(l = 0, flag = true; l < cnt; l++){
		if(!judge(k, base[l])){
		    flag = false;
		    break;
		}
	    }
	    if(flag)
		break;
	}
	printf("Case #%d: %d\n", j, k);
    }
    return 0;
}
