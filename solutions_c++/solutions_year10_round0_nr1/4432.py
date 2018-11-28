// Snapper Chain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int T;
int *N;
int *K;
int *OUT;
const int POWER_ON = 1;
const int POWER_OFF = 2;
const int NO_POWER_ON = 3;
const int NO_POWER_OFF = 4;

char *infilepath = "D:\\code jam\\Snapper Chain\\test.in";
char *outfilepath = "D:\\code jam\\Snapper Chain\\out.txt";

void readfile();
void writefile();
void init();

int _tmain(int argc, _TCHAR* argv[])
{
	readfile();
	init();
	writefile();
	delete[] N;
	delete[] K;
    delete[] OUT;
}

void readfile()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	infile>>T;
	infile.close();

	infile.open(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	char skip[20];
	infile.getline(skip, 20);
	N = new int[T];
	K = new int[T];
    OUT = new int[T];
	for(int i = 0; i < T; i++)
	{
		infile>>N[i]>>K[i];
	}
	infile.close();
}

void writefile()
{
	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	for(int i = 0; i < T; i++)
	{
        outfile<<"Case #"<<i + 1<<": "<<((OUT[i] == 0)?"OFF":"ON")<<'\n';
	}
	outfile.close();
}

void init()
{
    for(int i = 0; i < T; i++)
    {
        int NN = N[i]; 
        int KK = K[i];
        int* state = new int[NN];
        int* state_new = new int[NN];
        int *temp = 0;
        for(int j = 0; j < NN; j++) state[j] = NO_POWER_OFF;
        state[0] = POWER_OFF;
        for(int j = 0; j < KK; j++)
        {
            for(int k = 0; k < NN; k++) state_new[k] = state[k];
            state_new[0] = (state[0] == POWER_ON)?POWER_OFF:POWER_ON;
            for(int k = 1; k < NN; k++)
            {
                if(state[k] == POWER_ON) {
                    state_new[k] = POWER_OFF;
                }else if(state[k] == POWER_OFF) {
                    state_new[k] = POWER_ON;
                }
                if(state_new[k - 1] == POWER_ON){
                    switch(state_new[k]){
                        case NO_POWER_ON: state_new[k] = POWER_ON;break;
                        case NO_POWER_OFF: state_new[k] = POWER_OFF; break;
                        default:break;
                    }
                }else{
                    switch(state_new[k]){
                        case POWER_ON: state_new[k] = NO_POWER_ON;break;
                        case POWER_OFF: state_new[k] = NO_POWER_OFF; break;
                        default:break;
                    }
                }
            }
            temp = state;
            state = state_new;
            state_new = temp;
        }
        if(state[NN - 1] == POWER_ON){
            OUT[i] = 1;
        }else{
            OUT[i] = 0;
        }
        delete[] state;
        delete[] state_new;
    }
}

