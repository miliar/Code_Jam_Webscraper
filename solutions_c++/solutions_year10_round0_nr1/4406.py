/* 
 * File:   main.cpp
 * Author: enmand
 *
 * Created on May 8, 2010, 2:55 PM
 */

#include "Snapper.h"
#include <list>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv)
{
	long T;
	long *N = 0, *K = 0;
	ifstream input;

	input.open("input1");
	input >> T; // First line - Test Cases T

	N = new long[T]; // We have T cases for N
	K = new long[T]; // And T cases for K

	int i = 0; // Counter
	while(!input.eof())
	{
		input >> N[i]; input >> K[i];
		i++;
	}

	/**
	 * Now that we have our data, let's play with the Snappers
	 */
	for(int j = 0; j < T; j++) // Loop over each test case
	{
		cout << "Case #" << j+1 << ": ";
		Snapper *s = new Snapper[N[j]];
		// "Initialize" each snapper
		for(int k = 0; k < N[j] - 1; k++)
		{
			s[k].next = &s[k+1];
		}

		s[0].powerOn();
		for(int k = 0; k < K[j]; k++)
		{
			s[0].toggleOn();
		}
		if(s[0].lightOn() == 1)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
		delete[] s;
	}
	delete[] K; delete[] N;
	return (EXIT_SUCCESS);
}