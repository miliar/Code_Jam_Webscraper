/*
 * snapperchain.cpp
 *
 *  Created on: 07/05/2010
 *      Author: eduardoespinoza
 */

#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

//[0]=corriente [1]=on/off
void snap(vector<vector<int> > & mivectorsnappers) {
	int pos = 0;


	//actualizando estados
	for (int i = 0; i < mivectorsnappers[0].size(); ++i) {
		if (mivectorsnappers[0][i])
			mivectorsnappers[1][i] = !mivectorsnappers[1][i];
	}


	//actualizando los que reciben corriente
	for (int i = 0; i < mivectorsnappers[0].size()-1; ++i) {
		if (mivectorsnappers[1][i]&&mivectorsnappers[0][i]) //si esta prendido y tiene corriente
			mivectorsnappers[0][i+1] = 1;
		else
			mivectorsnappers[0][i+1] = 0;
	}

	//	while (mivectorsnappers[0][pos]) {//si recibe corriente
	//		//encenderlos
	//		mivectorsnappers[1][pos] = !mivectorsnappers[1][pos];
	//		if(mivectorsnappers[1][pos]&&mivectorsnappers[0][pos])
	//			mivectorsnappers[0][pos+1]=1;
	//		pos++;
	//	}
	//	pos = 0;
	//	while (mivectorsnappers[1][pos] && pos < mivectorsnappers[0].size() - 1) {
	//		mivectorsnappers[0][pos + 1] = mivectorsnappers[0][pos]&&mivectorsnappers[1][pos];
	//		pos++;
	//	}
}

void imprimir(vector<vector<int> > & mivectorsnappers) {

	printf("__________________________\n");
	printf("Corrie: ");
	for (int j = 0; j < mivectorsnappers[0].size(); ++j) {
		printf("%d->", mivectorsnappers[0][j]);
	}
	printf("\nOn/off: ");
	for (int j = 0; j < mivectorsnappers[1].size(); ++j) {
		printf("%d->", mivectorsnappers[1][j]);
	}
	printf("\n");

}

int main(int argc, char **argv) {

	int nrocasos;
	cin >> nrocasos;
	for (int i = 0; i < nrocasos; ++i) {
		int snappers, times;
		cin >> snappers >> times;
		vector<vector<int> > mivectorsnappers(2, vector<int> (snappers + 1, 0));
		mivectorsnappers[0][0] = 1;
//		imprimir(mivectorsnappers);
		for (int j = 0; j < times; ++j) {
			snap(mivectorsnappers);
//			imprimir(mivectorsnappers);
		}

		printf("Case #%d: %s\n" ,i+1,mivectorsnappers[0].back()?"ON":"OFF");

	}

	return 0;
}
