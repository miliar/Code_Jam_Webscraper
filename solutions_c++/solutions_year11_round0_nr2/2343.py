#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

static const size_t npos = -1;

// map base element to array index
int convert(char ch);

// check if there's overlap of characters in the two strings
bool hasOpposed(string elementList, string opposedList);

int main()
{

	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;
	cout << N << " num cases" << endl;

	for( int n = 0; n < N; n++ ) {
		string combine[8];
		string results[8];
		string opposed[8];

		int numCombos;
		fin >> numCombos;

		for( int i = 0; i < numCombos; i++ ) {
			string combo;
			fin >> combo;

			char base1 = combo[0];
			char base2 = combo[1];
			char result = combo[2];

			combine[convert(base1)] += base2;
			results[convert(base1)] += result;

			if( base1 != base2 ) {
				combine[convert(base2)] += base1;
				results[convert(base2)] += result;
			}
		}

		int numOpposed;
		fin >> numOpposed;

		for( int i = 0; i < numOpposed; i++ ) {
			string oppose;
			fin >> oppose;

			char base1 = oppose[0];
			char base2 = oppose[1];

			opposed[convert(base1)] += base2;
			opposed[convert(base2)] += base1;
		}

		int invokeLength;
		fin >> invokeLength;

		string invoked;
		fin >> invoked;

		string elementList = "";
		elementList += invoked[0];

		for( int i = 1; i < invoked.length(); i++ ) {
			char nextElement = invoked[i];

			if( elementList.length() == 0 ) {
				elementList += nextElement;
			}
			else {
				char lastElement = elementList[elementList.length()-1];

				int combineIndex = combine[convert(nextElement)].find(lastElement);

				if( combineIndex >= 0 ) {
					// replace last element with the new combined element
					elementList[elementList.length()-1] = results[convert(nextElement)][combineIndex];
				}
				else if ( hasOpposed(elementList, opposed[convert(nextElement)]) ) {
					elementList.clear();
				}
				else {
					elementList += nextElement;
				}
			}
		}

			
		cout << "Case #" << n+1 << ": " <<  "[";
		fout << "Case #" << n+1 << ": " <<  "[";
		
		if( elementList.length() > 0 ) {
			cout << elementList[0];
			fout << elementList[0];
		}
		for(int i = 1; i < elementList.length(); i++) {
			cout << ", ";
			fout << ", ";
			cout << elementList[i];
			fout << elementList[i];
		}
		cout << "]" << endl;
		fout << "]" << endl;
	}
		string x;
		cin >> x;

	return 0;
}

int convert(char ch)
{
	string x = "QWERASDF";
	return x.find(ch);
}
bool hasOpposed(string elementList, string opposedList)
{
	for( int i = 0; i < opposedList.length(); i++ ) {
		int foundIndex = elementList.find(opposedList[i]);
		if( foundIndex >= 0 && foundIndex != npos)
		{
			return true;
		}
	}
	return false;
}