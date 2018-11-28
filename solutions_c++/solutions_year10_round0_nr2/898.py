/* 
 * File:   main.cpp
 * Author: zhwang
 *
 * Created on May 8, 2010, 2:52 PM
 */

#include <stdlib.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
/*
 * 
 */
typedef unsigned long long int_64;
const int_64 MAX_INT64 = 99999999LL;
const int max_length = 7;

bool equalZERO(vector< int_64 > & a){
    for(int i = 0; i < a.size(); i++){
        if(a[i] != 0)
            return false;
    }
    return true;
}

bool greater_int64(vector< int_64 > & a, vector< int_64 > & b){
    if(a.size() < b.size())
        return false;
    else if(a.size() > b.size())
        return true;
    for(int i = 0; i < a.size(); i++){
        if(a[i] > b[i])
            return true;
        else if(a[i] < b[i])
            return false;
    }
    return false;
}

//copy b into a
void copy(vector< int_64 > & a, vector< int_64 > & b){
    a.resize(b.size(), 0);
    for(int i = 0; i < b.size(); i++){
        a[i] = b[i];
    }
}

//temp = a - b
void substract(vector< int_64 > & a, vector< int_64 > & b, vector< int_64 > & result){
    if(greater_int64(b,a)){
        substract(b, a, result);
        return;
    }
    if(result.size() != a.size())
        result.resize(a.size(), 0);
    int_64 flag = 0;

    for(int i = max_length - 1; i >= 0; i--){
		long temp = a[i] - flag;
        if(temp < b[i] || temp == -1){
            result[i] = a[i] - flag + MAX_INT64 + 1 - b[i];
            flag = 1;
        }
        else {
            result[i] = a[i] - flag - b[i];
            flag = 0;
        }
    }
}

int_64 divide(vector< int_64 > a, vector< int_64 > b){
    int_64 result = 0;
    while(greater_int64(a, b)){
        substract(a,b,a);
        result++;
    }
    return result;
}

void multi(vector< int_64 > & a, int_64 scale, vector< int_64 > & result){
    result.resize(a.size(),0);
    for(size_t i = a.size() - 1; i >= 1; i--){
        a[i - 1] += a[i] * scale / (MAX_INT64 + 1);
        result[i] = (a[i] * scale) % (MAX_INT64 + 1);
    }
}

//get gcd(a,b)
void gcd(vector< int_64 > a, vector< int_64 > b, vector< int_64 > & result){
    if( equalZERO(a)){
        copy(result, b);
		return;
    }

    while(!equalZERO(b)){
        if( greater_int64(a, b)){
            substract(a, b, a);           
        }
        else {
            substract(b, a, b);
        }
    }
    copy(result, a);
}



void Exchange(const string number, vector< int_64 > &arr2)
{
	vector< int_64 > arr;
    if("0" == number)
    {
        arr.push_back(-1);
        return;
    }
    int_64 temp;
    int length = number.size();
    int_64 j;
    int i;
    j = 1;
    temp = 0;
    for(i=length-1;i>=0;i--)
    {
        temp = temp + (number[i]-'0') * j;
        j *= 10;
        if(j > MAX_INT64)
        {
			arr.push_back(temp);
            j = 1;
            temp = 0;
        }
    }
    if(temp != 0)
        arr.push_back(temp);

	for(int i = arr.size() - 1; i >= 0; i--){
		arr2.push_back(arr[i]);
	}

    //padding 0 in front;
    while(arr2.size() < max_length){
        arr2.insert(arr2.begin(), 0LL);
    }
}
int main(int argc, char** argv) {
    ifstream fin("B-small-attempt1.in");
    if (!fin.is_open()) {
        cout << "can not open A-small.in" << endl;
        exit(-1);
    }
    int num_limits;
    fin >> num_limits;

    ofstream fout("B-small-attempt1.out");
    if (!fout.is_open()) {
        cout << "can not open A-small.out" << endl;
        exit(-1);
    }

    int num_times;
    
    for (long i = 0; i < num_limits; i++) {
        fin >> num_times;
        
        vector< vector< int_64 > >  itimeList(num_times);
        for(int t = 0; t < num_times; t++){
            string strTime;
            //getline(fin, strTime);
            fin >> strTime;
			
            Exchange(strTime, itimeList[t]);
        }
        vector< vector< int_64 > > itimediff(num_times - 1);
        for(int t = 0; t < num_times - 1; t++){
            substract(itimeList[t], itimeList[t+1], itimediff[t]);
        }
        vector<int_64> result;
		if(num_times - 1 > 1)
			gcd(itimediff[0], itimediff[1], result);
		else
			copy(result, itimediff[0]);
        for(int t = 2; t < num_times - 1; t++){
            gcd(result, itimediff[t], result);
        }

        vector< int_64 > min;
        for(int t = 0; t < max_length; t++){
            min.push_back(MAX_INT64);
        }
        for(int t = 0; t < num_times; t++){
            if(greater_int64(min, itimeList[t]))
                copy(min, itimeList[t]);
        }

        int_64 scale = divide(min, result);
        vector< int_64 > result2;
        multi(result, scale+1, result2);
        substract(result2, min, result);

        fout << "Case #" << i+1 << ": ";
        bool first = true;
        for(size_t t = 0; t < result.size(); t++){
            if(result[t] == 0 && first == true){
                if(t == result.size() - 1)
                    fout << 0;
            }
            else if(result[t] != 0 && first == true){
                fout << result[t];
                first = false;
            }
            else {
            fout.width(8);
            fout.fill(0);
            fout << result[t];
            }
        }
        fout << endl;
    }
    return (EXIT_SUCCESS);
}

