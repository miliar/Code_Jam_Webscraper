#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <fstream>
using namespace std;

unsigned long n,k;

void get_data(ifstream &inp);
int dec2bin(long decimal, int *bin);

int main()
{	
	string st;
	ifstream indata;
	cout << "Name of the file with the data: " << endl;
	cin >> st;
	indata.open(st.c_str());
	if (!indata.is_open())
	{
	cout << "Wrong file!" << endl;
	return 1;
	}
	cout << "Name the file with the output: " << endl;
	cin >> st;
	ofstream out(st.c_str());
	if(!out) {
	cout << "Cannot open file.\n";
	return 1;
	}
	int t;
	indata >>t;
	int bin[80];
	int tem;
	for (int i=0; i<t ;i++)
	{
		get_data(indata);
		for(int j=0; j<80;j++){
			bin[j]=0;
		}
		tem=dec2bin(k,bin);
		if(tem==0)
			out << "Case #" << i+1 << ": OFF" << endl;
		else
			out << "Case #" << i+1 << ": ON" << endl;
		//for(int j=0; j<80;j++){
		//	cout << " bin[" << j << "]= " << bin[j];
		//}
		//cout << "Case #" << i+1 << ": " << answer << endl;
	}
	//getchar();
	//getchar();
}
unsigned long getnum(unsigned long a)
{
	return (a%n);
}
void get_data(ifstream &inp)
{
	inp >> n;
	inp >> k;
}

int dec2bin(long decimal, int *binary)
{
int k = 0, h = 0;
int remain;
int old_decimal; 
int temp[80];
for(int j=0; j<80;j++){
	temp[j]=0;
}
do
{
old_decimal = decimal; 
remain = decimal % 2;
decimal = decimal / 2;
//printf("%d/2 = %d remainder = %d\n", old_decimal, decimal, remain);
temp[k] = remain;
k++;
} while (decimal > 0);
k--;
while (k >= 0){
binary[h] = temp[k];
h++;
k--;
}
for(int j=0; j<n;j++){
	//cout << binary[j];
	if (temp[j]==0)
		return 0;
}
return 1;
}