// GoogleCodeJam2012.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream arch(argv[1], ios::in);
	ofstream out("out.out");
    cout.rdbuf(out.rdbuf());
    char reem[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int cases;
    arch >> cases;
    char texto[101];
	arch.getline(texto, 101);
    for(int i=0;i<cases;i++)
    {
		arch.getline(texto, 101);
        for(int e=0;e<strlen(texto);e++)
                if(texto[e] != ' ')
                            texto[e] = reem[texto[e] - 'a'];
        cout << "Case #" << (i+1) << ": " << texto << endl;
    }
    arch.close();
	out.close();
}

