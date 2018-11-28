// DWtGooglers.cpp : main project file.

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace System;

using namespace System;
using namespace System::IO;
using namespace std;

//typedef vector<int, allocator<int> > INTVECTOR;


void bubbleSort(int *array,int length)//Bubble sort function 
{
    int i,j;
    for(i=0;i<length;i++)
    {
        for(j=0;j<length;j++)
        {
            if(array[i]>array[j])
            {
                int temp=array[i]; //swap 
                array[i]=array[j];
                array[j]=temp;
            }
        }
    }
}


void printElements(int *array,int length) //print array elements
{
    int i=0;
    for(i=0;i<length;i++)
        cout<<array[i]<<" , ";
	cout<<endl;
}


int call_result(int *array,int googlers,int Surprise,int limit){


	int Remaining=googlers;

	int result=0;

	int is_added=0;

	for(int i=0 ; i<googlers ; i++ ){
		Remaining = Remaining - 1;
		is_added = 0;

		cout<<"Value : "<<array[i]<<" , Remaining : "<<Remaining<<"  ,  Surprises rem : "<<Surprise<<" , REsult : "<<result<<endl;

		int temp_val;
		temp_val = array[i] - ( (array[i] / 3) * 3 );
		int diff = limit - (array[i] / 3);
	
		if(diff<=0){




			result = result + 1;
			//if(limit!=0){
			if(Remaining>=Surprise){    }
			else{	Surprise = Surprise - 1;
			}
		//	}
	//		else{
		//		if(Surprises>0){
	//				if(array[i]==2)

		//		}
		//	}

			}
		



		else if(diff==1){


			if(temp_val==0){
				if(array[i] == 0){

				}
				else if(array[i]>=3 && Surprise > 0){
				result = result+1;
				Surprise = Surprise - 1;
				}

			
			}
			
			if(temp_val==1){
				result = result +1;

			}
			else if(temp_val == 2){
				if(array[i]==2){
					if(Surprise<0){

					} else {
	result = result+1;
				Surprise = Surprise - 1;
					}
				}
				else {
									result = result +1;
				}	}
			
			


		} 
		else if (diff==2){

			if(temp_val == 2){
				if(Surprise>0){
				result = result + 1; 
				Surprise = Surprise - 1;
				}
			}
		
		}

		else if(diff>2){

		}


	//	if(is_added!=0){
//			result = result + 1;
	//	}


	}

 	
	cout<<"\n  Result  "<<result<<" \n ";
	getchar();

	return result;



}


int main(array<System::String ^> ^args)
{

	String^ fileName = "B-large.in";

	ifstream infile("B-large.in",ios::binary | ios::in );
	ofstream outfile("B-large.out",ios::binary | ios::out );

	int T;






	int N;
	int S;
	int p;

	int res=0;

	int temp;

	int scores[100];
	

	infile>>T;

	for(int i=1; i<=T; i++){
		outfile<<"Case #"<<i<<": ";
		res=0;

		infile>>N;
		infile>>S;
		infile>>p;
		
		cout<<N<<" , "<<S<<" , "<<p<<" : - >";

			for (int j=0; j<N ; j++ ){
			infile>>scores[j]; 
		}


		printElements(scores,N); 
	cout<<endl;
	bubbleSort(scores,N);                 //call to bubble sort  
    printElements(scores,N);               // print elements


	int temp_res = call_result(scores,N,S,p);
	outfile<<temp_res;
	//cout<<temp_res;


	//	for (int j=1; j<N ; j++ ){
	//	getchar();
	//	}

	outfile<<"\n";
	
	}

	return 0;
}



