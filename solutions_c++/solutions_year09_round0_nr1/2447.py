/*------------------------------------------------------------------------------
* Filename    :  allien.cpp
* Author      :  
* Description : 
*
* Date        :  Sep  2 2009 20:49:40
*
*-----------------------------------------------------------------------------*/

/* Includes ------------------------------------------------------------------*/
#include "stdio.h"
#include "allien.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/* Private Types -------------------------------------------------------------*/

/* Defines -------------------------------------------------------------------*/
#ifdef DEBUG
#define pr(a, ...) printf(a, __VA_ARGS__)
#else
#define pr(a, ...) 
#endif

#define LLEN	30

/* Function Declerations -----------------------------------------------------*/

/* Global Variables ----------------------------------------------------------*/
int n, l, d;
vector<string> w; 
vector<string> t; 
vector<char>   reg[LLEN];

/* Functions -----------------------------------------------------------------*/


/*------------------------------------------------------------------------------
* Function    :  main 
* Description :  main function 
*
* Params      :  int argc, char *argv[] 
* Returns     :  int 
*-----------------------------------------------------------------------------*/
int main(int argc, char *argv[])
{
	int i=0, ii=0, ij=0, ik=0;
	char str[(LLEN+2)*LLEN+1];
	string s;

	scanf("%d %d %d", &l, &d, &n);
	for(i=0; i<d; i++) {
		scanf("%s", str);
		s.assign(str);
		w.push_back(s);
	}

	for(i=0; i<n; i++) {
		scanf("%s", str);
		//gets(str);
		int j = 0, k=0;
		char c;
		int in = 0;
		for(ii=0; ii<l; ii++) reg[ii].clear();
		while((c=str[j]) != 0) {
			switch(c) {
				case '(':
					in = 1;
					break;
				case ')':
					in=0;
					k++;
					break;
				default:
					reg[k].push_back(c);
					if(in == 0) k++;
					break;
			}
			j++;
		}

		//for(ii=0; ii<k; ii++) cout<<reg[ii].size() << " " << endl;

		int found = 0;
		for(ii=0; ii<d; ii++) {
			const char *cp = w[ii].c_str();
			int il = 0;
			for(ij=0; ij<l; ij++) {
				for(ik=0; ik<reg[ij].size(); ik++) {
					if(reg[ij].at(ik) == cp[ij]) {
						il++;
						break;
					}
				}
			}
			if(il == l) found++;
		}
		cout << "Case #" << i+1 << ": " << found << endl;

	}


	pr("- L:%d - D:%d - N:%d - \n", l, d, n);

	return 0;
} /* main() */ 

/*------------------------------------------------------------------------------
* Function    :  
* Description : 
*
* Params      : 
* Returns     : 
*-----------------------------------------------------------------------------*/


/* vim: set ts=4 sw=4 sta si ff=unix: */


/* end of allien.c */
