// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"

#define stringSize 150

struct time {
	int hour;
	int minute;
	const time operator+(const time &other) {
		time result = *this;
		result.hour+=other.hour;
		result.minute+=other.minute;
		if (result.minute>59) { result.minute-=60; result.hour++; }
		return result;
	}
	const time operator+(const int &minute) {
		time result = *this;
		result.minute+=minute;
		if (result.minute>59) { result.minute-=60; result.hour++; }
		return result;
	}
	friend bool operator>=(const time& x, const time& y) {
		return (x.hour > y.hour || (x.hour == y.hour && x.minute>=y.minute));
	}
	friend bool operator>(const time& x, const time& y) {
		return (x.hour > y.hour || (x.hour == y.hour && x.minute>y.minute));
	}
	friend bool operator<(const time& x, const time& y) {
		return (x.hour < y.hour || (x.hour == y.hour && x.minute<y.minute));
	}

};

class stringList {
	struct node { char* string; node* next; };
	node* first;
	int size;
public:
	stringList(int sizeList) { 
		size = sizeList;
		first = new node; 
		node *pointer = first;
		for (int i=0; i<size; i++) {
			pointer->string = new char[stringSize];
			pointer->next = new node;
			pointer = pointer->next;
		}
	}
	~stringList() {
		node *pointer;
		for (int i=0; i<size; i++) {
			pointer = first;
			first = pointer->next;
			delete pointer->string;
			delete pointer;
		}
	}
	char*& operator[] (const int location) {
		node *pointer = first;
		for (int i=0; i<location; i++)
			pointer = pointer->next;
		return pointer->string;
	}
}; 

void ReadString(FILE *f, char *str) {
	char c;
	int p=0;
	do {
		c = fgetc(f);
		str[p++] = c;
	} while (!feof(f) && c!=0 && c!='\n' && c!=' ');
	str[p-1] = 0;
}

void ReadNumber(FILE *f, int &num) {
	char txt[100];
	ReadString(f,txt);
	num = atoi(txt);
}

void ReadTime(FILE *f, time &num) {
	char txt[100];
	int i;
	ReadString(f,txt);
	for (i=0; i<100; i++)
		if (txt[i]==':') break;
	txt[i]=0;
	num.hour = atoi(txt);
	num.minute = atoi(txt+i+1);
}


long long Pow(int a, int b) {
	long long v = 1;
	for (int i=0; i<b; i++) 
		v *= a;
	return v;
}

int FindChar(char item, char* str) {
	int len = strlen(str);
	for (int i=0; i<len; i++)
		if (item==str[i]) 
			return i;
	return 0;
}

void Run(time *TA, time *TA1, time *TB, time *TB1, int T, int numA, int numB) {
	int i,j, current, resultA = numA, resultB = numB;
	bool useA[100], useB[100], use;
	time t, t2;

	for (i=0; i<100; i++) {
		useA[i] = false;
		useB[i] = false;
	}

	for (i=0; i<numA; i++) {
		t = TA1[i] + T;
		use = false;
		for (j=0; j<numB; j++) {
			if (TB[j]>=t && useB[j]==false) {
				if (!use || TB[j]<t2) {
					use = true;
					t2 = TB[j];
					current = j;
		}	}	}
		if (use) {
			useB[current] = true;
			resultB--;
		}	
	}

	for (i=0; i<numB; i++) {
		t = TB1[i] + T;
		use = false;
		for (j=0; j<numA; j++) {
			if (TA[j]>=t && useA[j]==false) {
				if (!use || TA[j]<t2) {
					use = true;
					t2 = TA[j];
					current = j;
		}	}	}
		if (use) {
			useA[current] = true;
			resultA--;
		}	
	}

	printf("%d %d",resultA,resultB);
}

int _tmain(int argc, _TCHAR* argv[])
{
	time TA[100], TA1[100], TB[100], TB1[100];
	int T;
	int i, j, num, numA, numB;
	FILE *f;
	fopen_s(&f,"B-Small.in","r");
	if (!f) return 0;
	ReadNumber(f,num);
	for (i=0; i<num; i++) {
		////////////////
		// Read datas //
		////////////////
		ReadNumber(f,T);
		ReadNumber(f,numA);
		ReadNumber(f,numB);
		for (j=0; j<numA; j++) {
			ReadTime(f,TA[j]);
			ReadTime(f,TA1[j]);
		}
		for (j=0; j<numB; j++) {
			ReadTime(f,TB[j]);
			ReadTime(f,TB1[j]);
		}
		/////////////////
		// Show result //
		/////////////////
		printf("Case #%d: ",i+1);
		Run(TA, TA1, TB, TB1, T, numA, numB);
		printf("\n");
	}
	fclose(f);
	return 0;
}

