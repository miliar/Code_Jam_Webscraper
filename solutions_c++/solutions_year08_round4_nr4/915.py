#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int count(const char* str)
{
	int groups = 0;
	
	for(int i = 0; str[i]; i++) {		
		while(str[i+1] && str[i] == str[i+1]) i++;
		groups++;
	}
	return groups;
}

int main()
{
	int t, ans, k;
	char str[1010], buff[1010];
	cin >> t;
	
	for(int CASE = 1; CASE <= t; CASE++) {
				
		cin >> k >> str; //cout << "input: " << str << endl;
		strcpy(buff, str);
		ans = 100000000;
		
		int i, j;
		int len = strlen(str);
		int *arr = new int[k];
		
		for(i = 0; i < k; i++) arr[i] = i;
		
		do {
			for(i = 0; i < len; ) { 
				int ind = 0;
				for(j = i; j < k+i; j++, ind++) {// cout << "j: " << j << endl; 
					str[j] = buff[i + arr[ind]];					
				}
				i += k;
			}
			//cout << "temp: " << str << endl;
			int temp = count(str);
			if(temp < ans) ans = temp;
		} while(next_permutation(arr, arr + k));
		
		cout << "Case #" << CASE << ": " << ans << endl;
		
		delete [] arr;
	}	
	
	return 0;
}