// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;

struct Animal
{
	string name;
	vector<string> traits;
};


struct Tree{
	double weight;
	string feature;
	struct Tree* left;
	struct Tree* right;
} *root;


struct Tree * createTree(strstream& ss)
{
	
	char c;
	if (!ss.eof()) ss>> c;
	while ((c == ' ' || c == '\n' ) && (!ss.eof())) ss >> c;
	struct   Tree *t1 = new struct Tree ();
	t1->weight = 1.0;
	t1->left = NULL;
	t1->right = NULL;
	double weight;
	if (c == '(')
	{
		ss >> weight;
		ss >> c;
		t1->weight = weight;
		t1->left = NULL;
		t1->right = NULL;
		
		while ((c == ' ' || c == '\n' ) && (!ss.eof()) )ss >> c;
		if (c != ')') {
			ss.unget();
			ss >> t1->feature;
			t1->left = createTree(ss);
		
			t1->right = createTree(ss);
			ss>>c;
			while ((c == ' ' || c == '\n' ) && (!ss.eof()) )ss >> c;

		}
		else{
		
		//ss >> c;
		//while (c == ' ' || c == '\n') ss >> c;
		//if (c != ')')
			printf("dummy");
		}
	}


	return t1;

	
};


double getProb(struct Tree *t2, Animal a)
{
	double p = 1.0;
	struct Tree * currentNode;
	currentNode = t2;
	while (currentNode != NULL)
	{
		p = p * currentNode->weight;
		if (find(a.traits.begin(),a.traits.end(),currentNode->feature)!=a.traits.end()) currentNode = currentNode->left;
		else currentNode = currentNode->right;
	}
	return p;
}



int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	//repz(i,numCases);
	{
		int numTreelines;
		int numAnimals;
		string tree;
		vector<Animal> anml;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> numTreelines;
		repz(j,numTreelines)
		{
		   fin.getline(temp,2000);
		   tree += " " ;
		   tree += temp;
		   
		}
		fprintf(f2,"Case #%d:\n",i+1);
		strstream sstree;
		sstree << tree;
		struct Tree * mytree = createTree(sstree);

		fin.getline(temp,2000);
		strstream ss2;
		ss2 << temp;
		ss2 >> numAnimals;
		repz(j,numAnimals)
		{
			Animal a;
			strstream ss3;
			int ntr;
			fin.getline(temp,2000);
			ss3 << temp;
			ss3 >> a.name;
			ss3 >> ntr;
			repz(k,ntr) {
				string stemp;
				ss3 >> stemp;
				a.traits.push_back(stemp);
			}
			anml.push_back(a);
			fprintf(f2,"%.7lf\n",getProb(mytree,a));
			
		}
	
	
	}
	
	return 0;
}

