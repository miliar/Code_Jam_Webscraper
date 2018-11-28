// author : theycallhimavi
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <ctype.h>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <utility>
using namespace std;
/*inline long long read_int() {
char just_a_random_character;
while ((just_a_random_character=getchar_unlocked()) < 48 || just_a_random_character > 57);
long long row_loop = just_a_random_character-48;
while ((just_a_random_character=getchar_unlocked()) >= 48 && just_a_random_character <= 57) row_loop=row_loop*10+just_a_random_character-48;
return row_loop;
}*/

#define MAX(x,y) ((x)<(y) ? (y) : (x))
#define MIN(x,y) ((x)<(y) ? (x) : (y))
#define SWAP(x,y) do { a+=b; b=a-b; a=a-b; } while( 0 )
#define mod1 1000000007ll
#define mod2 10000007ll
#define inf 99999999999999999ll
#define REP(loop,n) for(loop=0;loop<n;loop++)
#define REPI(loop,j,n) for(loop=j;loop<n;loop++)
#define PER(loop,n) for(loop=n-1;loop>=0;loop--)
typedef vector<long long> vi;
typedef pair<long long, long long> ii;

template <class T>
T power(T x,T y,T m)
{
	T temp;
	if( y == 0)
		return 1;
	temp = power(x,y/2,m)%m;
	if (y%2 == 0)
		return ((temp % m)*(temp% m))%m;
	else
		return (((((x)*(temp))%m)*(temp))%m)%m;
}


long long Global_selector = 0;

long long dfs_get_it_done(vector<vector<char>> originals,long long row_loop, long long coloumn_loop, char just_a_random_character) {
	long long count = 0;
	for(long long loop = 0; loop < 4; loop++){
		if(originals[loop][coloumn_loop] == just_a_random_character || originals[loop][coloumn_loop] == 'T'){
			count++;
			if(count == 4)
				return count;
		}
		else
			break;
	}
	count = 0;
	for(long long loop = 0; loop < 4; loop++){
		if(originals[row_loop][loop] == just_a_random_character || originals[row_loop][loop] == 'T'){
			count++;
			if(count == 4)
				return count;
		}
		else
			break;
	}
	count = 0;
	if(row_loop == coloumn_loop){
		if((originals[0][0] == just_a_random_character || originals[0][0] == 'T') && (originals[1][1] == just_a_random_character || originals[1][1] == 'T') && (originals[2][2] == just_a_random_character || originals[2][2] == 'T') && (originals[3][3] == just_a_random_character || originals[3][3] == 'T')){
			count = 4;
			return count;
		}
	}
	if((row_loop == 1 && coloumn_loop==2) || (row_loop==2 && coloumn_loop==1) || (row_loop==3 && coloumn_loop==0) || (row_loop==0 && coloumn_loop==3)){
		if((originals[3][0] == just_a_random_character || originals[3][0] == 'T') && (originals[2][1] == just_a_random_character || originals[2][1] == 'T') && (originals[1][2] == just_a_random_character || originals[1][2] == 'T') && (originals[0][3] == just_a_random_character || originals[0][3] == 'T')){
			count = 4;
			return count;
		}
	}
	return 0;
}

int main(){
	long long cases,X;
	vector<long long>Global_selectorX;
	cin>>cases;
	for(long long Y = 1; Y <= cases; Y++){
	    vector<long long> P_random;
		long long Random_integer,Just_a_random_auxillary_variable,Just_a_random_original_variable;
		Random_integer = Just_a_random_auxillary_variable = Just_a_random_original_variable = 0;
		char the_status_which_is_to_be_obtained,bv;
		vector<vector<char> >brr(4,vector<char>(4,'c'));
		for(long long loop = 0; loop < 4; loop++){
			for(long long j = 0; j < 4; j++){
				cin >> the_status_which_is_to_be_obtained;
				brr[loop][j] = the_status_which_is_to_be_obtained;
			}
		}
		for(long long loop = 0; loop < 4; loop++){
			for(long long j = 0; j < 4; j++){
				if(brr[loop][j] == '.')
					Random_integer = 1;
				if(brr[loop][j] == 'X')
					Just_a_random_auxillary_variable = dfs_get_it_done(brr,loop,j,brr[loop][j]);
				if(brr[loop][j] == 'O')
					Just_a_random_original_variable = dfs_get_it_done(brr,loop,j,brr[loop][j]);
			}
			if(Just_a_random_auxillary_variable == 4 || Just_a_random_original_variable == 4)
				break;
		}
        if(Just_a_random_auxillary_variable == 4)
			cout<<"Case #"<<Y<<": "<< "X won"<<endl;
        if(Just_a_random_original_variable == 4)
            cout <<"Case #"<<Y<<": "<< "O won" << endl;
        if(Just_a_random_auxillary_variable != 4 && Just_a_random_original_variable != 4) {
			if(Random_integer == 1)
				cout<<"Case #"<<Y<<": "<<"Game has not completed"<<endl;
		}
		if(Just_a_random_auxillary_variable != 4 && Just_a_random_original_variable != 4){
			if(Random_integer == 0)
				cout <<"Case #"<<Y<<": "<< "Draw" << endl;
		}
	}
	return 0;
}