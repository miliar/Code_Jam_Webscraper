// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>

void readInput();
void switchFind(int&,int&,std::string*,std::string*,int&,int,std::string);
std::string getString(int&,int&,std::string*,std::string*,int&,std::string&);

// TODO: reference additional headers your program requires here
