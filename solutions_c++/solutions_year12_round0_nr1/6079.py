//============================================================================
// Name        : GoogleCodeJam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<string.h>
#include <iostream>
using namespace std;

char ch(char ch){
	//a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
	char map[] ={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	return map[ch-'a'];
}

void change(char str[]){
	for(int i = 0 ;i<strlen(str);i++){
		if(str[i] != 32 )
			str[i] = ch(str[i]);
	}
}

int main() {
	int n = 0 ;
	char str[200];
	scanf("%d\n",&n);
	//printf("Output\n");
	for(int i =0;i<n;i++){
		cin.getline(str,110);
		change(str);
		printf("Case #%d: %s\n",i+1,str);
	}
	return 0;
}
