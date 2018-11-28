#include<iostream>
#include<iomanip>
#include<stdlib.h>
#include<string.h>
#define NN 100
using namespace std;

class BigN{
    public:
	char values[NN];
	BigN(){
	}
	int len(){
	    return strlen(values);
	}
	void set(char* value){
	    strcpy(values, value);
	}
	void print(){
	    cout << values << endl;
	}
	BigN diff(BigN &b){
	    BigN *big, *small;
	    if( *this > b ){
		big = this;
		small = &b;
	    }else{
		small = this;
		big = &b;
	    }
	    char value[NN];
	    int carry = 0, idx = NN, tmp = 0, ptr = 0;
	    value[--idx] = '\0';
	    for(int bl = big->len(), sl = small->len() ; ptr < sl ; ptr++ ){
		tmp = (big->values[bl-ptr-1] - small->values[sl-ptr-1]) - carry;
		if( tmp < 0 ){
		    tmp += 10;
		    carry = 1;
		}else{
		    carry = 0;
		}
		value[--idx] = '0' + tmp;
	    }
	    for(int bl = big->len() ; ptr < bl ; ptr++){
		tmp = (big->values[bl-ptr-1] - '0') - carry;
		if( tmp < 0 ){
		    tmp += 10;
		    carry = 1;
		}else{
		    carry = 0;
		}
		value[--idx] = '0' + tmp;
	    }
	    while(value[idx] == '0'){
		idx++;
	    }
	    BigN result;
	    result.set( &(value[idx]) );
	    return result;
	}
	bool operator <(BigN &b){
	    if(this->len() != b.len()){
		//cout << "small? " << this->values << " != " << b.values << endl;
		return this->len() < b.len();
	    }
	    int idx = 0;
	    while(idx < this->len() && this->values[idx] == b.values[idx]){
		idx++;
	    }
	    return this->values[idx] < b.values[idx];
	}
	bool operator >(BigN &b){
	    if(this->len() != b.len()){
		return this->len() > b.len();
	    }
	    int idx = 0;
	    while(idx < this->len() && this->values[idx] == b.values[idx]){
		idx++;
	    }
	    return this->values[idx] > b.values[idx];
	}
	bool operator ==(BigN &b){
	    if( *this < b || *this > b ){
		return false;
	    }
	    return true;
	}
};

void show(unsigned int N, BigN T[]){
    for(int i = 0 ; i < N ; i++){
	cout << "\t" << T[i].values << endl;
    }
}

BigN apocalypse(unsigned int N, BigN T[]){
    BigN numbers[N-1];
    for(int i = 0 ; i < N-1 ; i++){
	numbers[i] = T[i].diff( T[N-1] );
    }
    BigN smallest;
    for(int i = 0 ; i < N-1 ; i++){
	if( numbers[i].len() > 0 ){
	    smallest.set( numbers[i].values );
	    break;
	}
    }
    //show(N-1, numbers);
    int size = N-1;
    while(size > 0){
	//cout << "size:" << size << endl;
	//show(size, numbers);
	for( int i = 0 ; i < size ; i++ ){
	    while(numbers[i] > smallest || numbers[i] == smallest ){
		//cout << "number[" << i << "/" << size << "]:" << numbers[i].values << " smallest:" << smallest.values << endl;
		numbers[i].set( numbers[i].diff( smallest ).values );
	    }
	    if( numbers[i].len() == 0 ){
		numbers[i].set( numbers[--size].values );
		i--;
	    }else{
		while( smallest > numbers[i] ){
		    smallest.set( smallest.diff( numbers[i] ).values );
		}
	    }
	}
    }

    BigN nearest = T[0], diff;
    for(int i = 1 ; i < N ; i++){
	if( T[i] < nearest ){
	    nearest.set( T[i].values );
	}
    }
    diff.set( nearest.values );
    while( diff > smallest ){
	diff.set( diff.diff(smallest).values );
    }
    if( diff.len() > 0 ){
	diff.set( diff.diff(smallest).values );
    }
    return diff;
}


int main(int argc, char* argv[]){
    unsigned int C, N;
    BigN T[1005];
    char in[100];
    cin >> C;
    for(int i = 0 ; i < C ; i++){
	cin >> N;
	for(int j = 0 ; j < N ; j++){
	    cin >> in;
	    T[j].set(in);
	}
	BigN gcd_diff = apocalypse(N, T);
	cout << "Case #" << i+1 << ": " << (gcd_diff.len() > 0 ? gcd_diff.values : "0") << endl;
    }
    return 0;
}
