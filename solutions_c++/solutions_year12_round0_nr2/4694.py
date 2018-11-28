// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

void bubbleSort(int*);

int main(int argc, char *argv[])
{
    ifstream arch(argv[1], ios::in);
	ofstream out("out.out");
    cout.rdbuf(out.rdbuf());
    int t;
    arch >> t;
    for(int i=0;i<t;i++)
    {
		int n,s,p;
		arch >> n >> s >> p;
		int* g = new int[n];
		for(int e=0;e<n;e++)
			arch >> g[e];
		bubbleSort(g);
		int min=(p <= 2) ? p : p + 2*(p-2);
		int norm=(p <= 1) ? p : p + 2*(p-1);
		int cuantos=0;
		for(int e=0;e<n;e++)
		{
			if(g[e] >= norm) cuantos++;
			else if(g[e] >= min && s) {
				cuantos++;
				s--;
			}
		}
		cout << "Case #" << (i+1) << ": " << cuantos << endl;
		delete g;
    }
    arch.close();
	out.close();
}

void bubbleSort(int* arr) {
      bool swapped = true;
      int j = 0;
      int tmp,tam=sizeof(arr)/sizeof(int);
      while (swapped) {
            swapped = false;
            j++;
            for (int i = 0; i < tam - j; i++) {
                  if (arr[i] > arr[i + 1]) {
                        tmp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = tmp;
                        swapped = true;
                  }
            }
      }
}