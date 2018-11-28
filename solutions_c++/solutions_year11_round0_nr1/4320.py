#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string> 
#include <vector>
#include <algorithm>

    using namespace std;

void swap(int *x,int *y)
{
   int temp;
   temp = *x;
   *x = *y;
   *y = temp;
}

void swap2(char *x,char *y)
{
   char temp;
   temp = *x;
   *x = *y;
   *y = temp;
}

void bublesort2(int list[], char list2[], int n)
{

   int i,j;
   for(i=0;i<(n-1);i++)
      for(j=0;j<(n-(i+1));j++)
             if(list[j] > list[j+1])
			 {
                    swap(&list[j],&list[j+1]);
					swap2(&list2[j],&list2[j+1]);
			 }
}

int main()
{
	int T, N, p[100];
	char  r[100];

	ifstream fp_in;
	ofstream fp_out;
	fp_in.open("A-large.in", ios::in);
	fp_out.open("test.out",ios::out);

	fp_in >> T;
	cout << T << endl;
	for(int i=0;i<T;i++)
	{
		fp_in >> N;
	//	cout << "N="<<N<<endl;
		for(int k=0;k<N;k++){
			fp_in >> r[k];  //robot
			fp_in >> p[k]; // button instruction
	//		cout <<"p["<<k<<"]="<<p[k]<<" r="<<r[k]<<endl;
		}

		int z=0,y=0, Bp[100],Op[100];
		for(int k=0;k<N;k++){

			if(r[k] == 'B'){
			Bp[z]=p[k]; 
	//		cout <<"Bp["<<z<<"]="<<Bp[z]<<endl;
			z++;
			}
			else{
				Op[y]=p[k]; 
	//			cout <<"Op["<<y<<"]="<<Op[y]<<endl;
				y++;
			}

		//	cout << "Bp=" << Bp[z]<<" Op="<<Op[y]<<endl;
		}
	//	bublesort2(p,r,N);
		//for(int k=0;k<N;k++){
		//	cout <<"p["<<k<<"]="<<p[k]<<" r="<<r[k]<<endl;
		//}
		z=0;
		y=0;
		int t=0, k=0,Bpos=1, Opos=1, ball=0, bon,oon;  //Ball 0=blue, 1=Orange
		while(k<N)
		{
			bon=1;
			oon=1;
	//		cout << "Bp=" << Bp[z]<<" Bpos="<<Bpos<<" Op="<<Op[y]<<" Opos="<<Opos<<endl;
			switch(r[k]){
				case 'B':
					if(p[k] == Bpos){
						k++; z++;   //push it, advance instrciont
						bon=0; //turn off for this t
					}
					break;
				case 'O':
					if(p[k] == Opos){
						k++; y++;    //push it, advance instruction
						oon=0; //turn off for this t
					}
					break;
				}
			//Now move in the right direction if you have to, only if you haven't arleady pushed a button
			if(bon){
			if (Bp[z] - Bpos > 0)
				Bpos++;
			if (Bpos - Bp[z] > 0 && Bpos > 0)
				Bpos--;
			}

			if(oon){
			if (Op[y] - Opos > 0)
				Opos++;
			if (Opos - Op[y] > 0 && Opos > 0)
				Opos--;
			}
			t++;

		}

		
		fp_out <<"Case #" << i+1 <<": "<<t<<endl;
		cout <<"Case #" << i+1 <<": "<<t<<endl;
		//while (k < N)
		//{
		//	
		//}
	}
	system("PAUSE");
	fp_in.close();
	fp_out.close();
	return 0;
}

