/*
 * ql_1a.cpp
 *
 *  Created on: May 21, 2010
 *      Author: root
 */

#include "ql_1a.h"

#include <gmp.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define MacroSwap(a,b) (((a)^=(b)),((b)^=(a)),((a)^=(b)))

void print_matrix(int **matrix, int row, int col){

	cout << "========================================" << endl;
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++)
			cout << matrix[i][j] << " ";
		cout << endl;
	}
	cout << "========================================" << endl;

}

void ql_1a::quiz1(){

	ifstream input("A-large.in");
	ofstream output("A-large.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){
		int N=0,K=0;
		if(input>>tmp)
			N=atoi(tmp.c_str());
		if(input>>tmp)
			K=atoi(tmp.c_str());
		cout << N << "\t" << K << endl;
		int **m = new int*[N];
		for(int i=0;i<N;i++)
			m[i]=new int[N];
		for(int i=0;i<N;i++){
			if(input>>tmp){
				for(int j=0;j<N;j++){
					if(tmp[j]=='.')
						m[i][j]=0;
					else if(tmp[j]=='R')
						m[i][j]=1;
					else
						m[i][j]=2;
				}
				/*
				if(!strcmp((char *)(tmp.c_str()),"."))
					m[i][j]=0;
				else if(!strcmp((char *)(tmp.c_str()),"R"))
					m[i][j]=1;	//R == 1
				else
					m[i][j]=2;*/

			}
		}
		//print_matrix(m,N,N);
		/*
		//transform
		for(int i=0;i<N;i++){
			for(int j=i;j<N;j++){
				if(i!=j)
					MacroSwap(m[i][j],m[j][i]);
			}
		}

		//print_matrix(m,N,N);
		//reverse by col
		for(int i=0;i<N;i++)
			for(int j=0;j<N/2;j++)
				MacroSwap(m[i][j],m[i][N-j-1]);
		//print_matrix(m,N,N);
		 *
		 */

		//gravity
		for(int col=0;col<N;col++){
			int ptr1=N-1, ptr2=N-1;
				while(ptr2>=0){
					if(m[col][ptr2]!=0)
						m[col][ptr1--]=m[col][ptr2--];
					else{
						ptr2--;
					}
				}
				while(ptr1>=0)
					m[col][ptr1--]=0;
		}
		//print_matrix(m,N,N);

		bool red=false,blue=false,both=false;

		for(int i=0;i<N;i++){
			int h_red=0,h_blue=0,v_red=0,v_blue=0,d_red_l=0,d_red_r=0,d_blue_l=0,d_blue_r=0,ad_red_l=0,ad_red_r=0,ad_blue_l=0,ad_blue_r=0;
			for(int j=0;j<N;j++){
				//check the horizontal
				if(m[i][j]==1)
					h_red++;
				else
					h_red=0;
				if(m[i][j]==2)
					h_blue++;
				else
					h_blue=0;

				//check the vertical
				if(m[j][i]==1)
					v_red++;
				else
					v_red=0;
				if(m[j][i]==2)
					v_blue++;
				else
					v_blue=0;

				//check the diagonal
				if(!i){	//diagonal, middle to two side (up to down), left to right
					if(m[j][j]==1)
						d_red_l++;
					else
						d_red_l=0;
					if(m[j][j]==2)
						d_blue_l++;
					else
						d_blue_l=0;
				}
				else{
					if(i+j<N){
						if(m[j][j+i]==1)
							d_red_l++;
						else
							d_red_l=0;
						if(m[j][j+i]==2)
							d_blue_l++;
						else
							d_blue_l=0;

						if(m[j+i][j]==1)
							d_red_r++;
						else
							d_red_r=0;
						if(m[j+i][j]==2)
							d_blue_r++;
						else
							d_blue_r=0;
					}
				}

				if(!i){	//anti-diagonal, middle to two side (down to up), left to rightt
					if(m[j][N-j-1]==1)
						ad_red_l++;
					else
						ad_red_l=0;
					if(m[j][N-j-1]==2)
						ad_blue_l++;
					else
						ad_blue_l=0;
				}
				else{
					if(N-j-1-i >= 0){
						if(m[j][N-j-1-i]==1)
							ad_red_l++;
						else
							ad_red_l=0;
						if(m[j][N-j-1-i]==2)
							ad_blue_l++;
						else
							ad_blue_l=0;
					}

					if(i+j < N){
						if(m[j+i][N-j-1]==1)
							ad_red_r++;
						else
							ad_red_r=0;
						if(m[j+i][N-j-1]==2)
							ad_blue_r++;
						else
							ad_blue_r=0;
					}

				}
/////////////

				if(h_red==K || v_red==K || d_red_l==K || d_red_r==K || ad_red_l==K || ad_red_r==K)
					red=true;
				if(h_blue==K || v_blue==K || d_blue_l==K || d_blue_r==K || ad_blue_l==K || ad_blue_r==K)
					blue=true;
				if(red && blue){
					both=true;
					break;
				}
			}

			if(both)
				break;
		}

		string result="";
		if(both)
			result="Both";
		else if(red)
			result="Red";
		else if(blue)
			result="Blue";
		else
			result="Neither";

		for(int i=0;i<N;i++)
			delete[] m[i];
		delete[] m;

		//int stop;cin>>stop;
		output << "Case #" << count << ": " << result << endl;
		cout << result << endl;
		count++;
	}


	input.close();
	output.close();
}

void ql_1a::quiz2(){

	ifstream input("B-small.in");
	ofstream output("B-small.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){


		//output << "Case #" << count << ": " << result << endl;
		count++;
	}


	input.close();
	output.close();
}

void ql_1a::quiz3(){

	ifstream input("C-test.in");
	ofstream output("C-test.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){
		long long A1=0,A2=0,B1=0,B2=0;
		if(input>>tmp)
			A1=atoi(tmp.c_str());
		if(input>>tmp)
			A2=atoi(tmp.c_str());
		if(input>>tmp)
			B1=atoi(tmp.c_str());
		if(input>>tmp)
			B2=atoi(tmp.c_str());

		long long wins=0;
		for(long long a=A1;a<=A2;a++){
			for(long long b=B1;b<=B2;b++){
				if(a==b)
					continue;
				while(a!=b && a>=0 && b>=0){
					if(a>b){
						if(a/b>=2){
							if(a%b==0)
								wins++;
							else
								a=(a%b+b);
						}
					}
					else if(a<b){
						if(b/2>=2){
							if(b%a==0)
								wins++;
							else
								b=(b%a+a);
						}
					}
				}

			}
		}
		output << "Case #" << count << ": " << wins << endl;
		count++;
	}


	input.close();
	output.close();
}

/*
 * The Second Part of OL test 1
 *
 * Author: Yimin Song
 *
 * Date: May 22th. 2010
 *
 **********************************************************************************************************************************************************
 **********************************************************************************************************************************************************
 **********************************************************************************************************************************************************
 */

void ql_1a::quizb1(){
	ifstream input("A-test.in");
	ofstream output("A-test.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){
		int N=0,M=0;
		if(input>>tmp)
			N=atoi(tmp.c_str());
		//cout << tmp << endl;
		int stop1;cin>>stop1;
		if(input>>tmp)
			M=atoi(tmp.c_str());
		//cout << tmp << endl;
		int stop2;cin>>stop2;
		//string *tmpstr=new string[N];
		map<string, vector<string> > direc;
		for(int i=0;i<N;i++){
			string dirlist[1024];
			int listptr=0;
			if(input>>tmp){
				cout << tmp << endl;
				char *pch;
				pch=strtok((char *)tmp.c_str(),"/");
				dirlist[listptr++]=pch;
				while(pch){
					pch=strtok(NULL,"/");
					dirlist[listptr++]=pch;
				}
				cout << pch << endl;
				int stop;cin>>stop;
				/*				map<string, vector<string> >::iterator it;
				vector<string> emptyvec;
				direc[(string)pch]=emptyvec;
				 *
				 *
				 * 					if(find(direc[parent].begin(),direc[parent].end(),(string)pch) != direc[parent].end()){

					}
				 */
			}
		}
		//output << "Case #" << count << ": " << wins << endl;
		count++;
	}


	input.close();
	output.close();

}

void ql_1a::quizb2(){
	ifstream input("B-large.in");
	ofstream output("B-large.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int round=0;
	string tmp;
	while(!input.eof() && round < num_){
		int N,K,B,T;
		input>>N>>K>>B>>T;
		vector<int> location;
		vector<int> speed;
		for(int j=0;j<N;j++)
		{
			int t;
			input>>t;
			location.push_back(t);
		}
		for(int j=0;j<N;j++)
		{
			int t;
			input>>t;
			speed.push_back(t);
		}

		vector<float> time(N);
		for(int j=0;j<N;j++)
		{
			time[j]=(float)(B-location[j])/speed[j];
		}

		int sum=0;
		for(int j=0;j<N;j++)
		{
			if(time[j]<=T)
				sum++;
		}
		if(sum<K)
		{
			output<<"Case #"<<round+1<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			sum=0;
			int count=0;
			for(int j=N-1;j>=0;j--)
			{
				if(time[j]<=T)
				{
					sum++;
					for(int l=j+1;l<N;l++)
					{
						if(time[l]>T) count++;
					}
					if(sum==K) break;
				}
			}
			output<<"Case #"<<round+1<<": "<<count<<endl;
		}
		round++;
	}


	input.close();
	output.close();
}

void find_fb_ite_all(){
	mpz_t fb[500];
	mpz_init(fb[0]);
	mpz_init(fb[1]);
	mpz_set_ui(fb[0],1);
	mpz_set_ui(fb[1],2);

	char *str1 = new char[mpz_sizeinbase(fb[0],10)];
	mpz_get_str(str1,10,fb[0]);

	char *str2 = new char[mpz_sizeinbase(fb[1],10)];
	mpz_get_str(str2,10,fb[1]);

	cout << str1 << endl << str2 << endl;

	mpz_t prev1,prev2;
	mpz_init(prev1);
	mpz_init(prev2);
	mpz_set_ui(prev1,1);
	mpz_set_ui(prev2,1);

	mpz_t crnt;
	mpz_init(crnt);
	mpz_add(crnt,prev1,prev2);

	int cnt=2;
	while(cnt<500){
		mpz_set(prev2,prev1);
		mpz_set(prev1,crnt);

		mpz_t tmpcrnt;
		mpz_init(tmpcrnt);

		mpz_add(tmpcrnt,prev1,prev2);
		mpz_mod_ui(crnt,tmpcrnt,100003);

		mpz_init(fb[cnt]);
		mpz_set(fb[cnt],crnt);

		char *strtest = new char[mpz_sizeinbase(fb[cnt],10)];
		mpz_get_str(strtest,10,fb[cnt]);

		cout << strtest << endl;

		cnt++;
	}
}

void ql_1a::quizb3(){
	string fb[500];
	fb[0]="0";
	fb[1]="1";

	//cout << fb[0] << endl << fb[1] << endl;

	mpz_t prev1,prev2;
	mpz_init(prev1);
	mpz_init(prev2);
	mpz_set_ui(prev1,0);
	mpz_set_ui(prev2,1);

	mpz_t crnt;
	mpz_init(crnt);
	mpz_add(crnt,prev1,prev2);

	int cnt=2;
	while(cnt<500){
		mpz_set(prev2,prev1);
		mpz_set(prev1,crnt);

		mpz_add(crnt,prev1,prev2);

		mpz_t tmpcrnt;
		mpz_init(tmpcrnt);
		mpz_mod_ui(tmpcrnt,crnt,100003);
		//mpz_set(tmpcrnt,crnt);

		//mpz_init(fb[cnt]);
		//mpz_set(fb[cnt],tmpcrnt);

		char *strtest = new char[mpz_sizeinbase(tmpcrnt,10)];
		mpz_get_str(strtest,10,tmpcrnt);
		fb[cnt]=strtest;

		//cout << fb[cnt] << endl;

		cnt++;
	}


	ifstream input("C-small-attempt0.in");
	ofstream output("C-small-attempt0.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){
		int N=0;
		input>>N;

		output << "Case #" << count << ": " << fb[N] << endl;
		count++;
	}


	input.close();
	output.close();

}

void ql_1a::quizb32(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    for(int i=0;i<maxn;i++){
        C[i][0]=1;
        for(int j=1;j<=i;j++)
            C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
    }
    for(int i=2;i<maxn;i++){
        f[i][1]=1;
        for(int j=2;j<i;j++){
            f[i][j]=0;
            for(int k=0;k<=j-2;k++){
                f[i][j]=(f[i][j]+f[j][j-k-1]*C[i-j-1][k])%mod;
            }
        }
    }
    int Tn;
    scanf("%d", &Tn);
    for (int T = 1; T <= Tn; T++) {
        int n;
    	scanf("%d",&n);
    	printf("Case #%d: ", T);
    	LL ans=0;
    	for(int i=1;i<n;i++)
            ans=(ans+f[n][i])%mod;
    	printf("%I64d\n",ans);
    }
	return;

}

ql_1a::ql_1a(){

	return;
}

ql_1a::~ql_1a(){

}

int main(){


	ql_1a quiz;
	quiz.quizb32();
	//find_fb_ite_all();
/*
	mpz_t op1,op2,result;
	mpz_init(op1);
	mpz_init(op2);
	mpz_init(result);
	mpz_set_str(op1,"263816287362187361872638216387213",9);
	char *strtmp = new char[mpz_sizeinbase(op1,10)];
	mpz_get_str(strtmp,10,op1);
	cout << strtmp << endl;

	mpz_set_str(op2,"89798798797387987870575858768216387213",10);

	mpz_add(result,op1,op2);
	mpz_div(result,op2,result);
	mpz_sub(result,result,op1);
	mpz_abs(result,result);
	mpz_mod_ui(result,result,10);

	char *strtest = new char[mpz_sizeinbase(result,10)];
	mpz_get_str(strtest,10,result);

	cout << strtest << endl;
*/

	//cout << "done!" << endl;
	return 0;
}
