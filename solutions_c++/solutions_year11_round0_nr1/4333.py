/* 
 * File:   main.cpp
 * Author: Divij
 *
 * Created on 7 May, 2011, 4:41 AM
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>

using namespace std;

int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    scanf("%d",&T);

    for(int l=0;l<T;l++){
	int N;
	scanf("%d",&N);

	vector<bool> test(N,true);//true denotes orage turn
	vector<int> blue;
	vector<int> orange;
	char ch;
	int num=0;
	for(int i=0;i<N;i++){
	    cin >> ch;
	    scanf("%d",&num);
	    if(ch=='O'){
		test[i]=true;
		orange.push_back(num);
	    }else{
		test[i]=false;
		blue.push_back(num);
	    }
	    
	}
	/*for(int i=0;i<test.size();i++){
	    cout << test[i] << " ";
	}cout << endl;*/
	int counter=0;
	int pos_o=1;
	int pos_b=1;
	int dest_o=0;
	int dest_b=0;
	for(int i=0;i<N;i++){
	    int time=0;
	    if(test[i]){
		//orange turn
		time=(abs(pos_o-orange[dest_o]))+1;
		pos_o=orange[dest_o];
		counter+=time;
		dest_o++;
		if(dest_b<blue.size()){
		    if(abs(pos_b-blue[dest_b])<=time){
			pos_b=blue[dest_b];
		    }else{
			if(pos_b>blue[dest_b]){
			    pos_b-=time;
			}else{
			    pos_b+=time;
			}
		    }
		}
	    }else{
		//blue turn
		time=(abs(pos_b-blue[dest_b]))+1;
		pos_b=blue[dest_b];
		counter+=time;
		dest_b++;
		if(dest_o<orange.size()){
		    if(abs(pos_o-orange[dest_o])<=time){
			pos_o=orange[dest_o];
		    }else{
			if(pos_o>orange[dest_o]){
			    pos_o-=time;
			}else{
			    pos_o+=time;
			}
		    }
		}
	    }
	}

	printf("Case #%d: %d\n",l+1,counter);

    }
    fclose(stdout);
    fclose(stdout);
    return 0;
}

