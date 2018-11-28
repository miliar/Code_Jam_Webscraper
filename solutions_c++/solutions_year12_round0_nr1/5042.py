// GoogleCodeJam-cpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
/*    const char* testcaseInput[3];
    testcaseInput[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    testcaseInput[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    testcaseInput[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

    const char* testcaseOutput[3];
    testcaseOutput[0] = "our language is impossible to understand";
    testcaseOutput[1] = "there are twenty six factorial possibilities";
    testcaseOutput[2] = "so it is okay if you want to just give up";

	char map[27];	// zero terminated for printing
	memset(map, '?', 26);
	map[26] = 0;
	for (int nCase = 0; nCase < 3; nCase++)
	{
		for (unsigned int nIndex = 0; nIndex < strlen(testcaseInput[nCase]); nIndex++)
		{
			map[int(testcaseInput[nCase][nIndex] - 'a')] = testcaseOutput[nCase][nIndex];
		}
	}
	printf(map);
	_getch();*/

/*	char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
    const char* testcaseInput[3];
    testcaseInput[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    testcaseInput[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    testcaseInput[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char testcaseOutput[100];

	for (int nCase = 0; nCase < 3; nCase++)
	{
		for (unsigned int nIndex = 0; nIndex < strlen(testcaseInput[nCase]); nIndex++)
		{
			if (' ' == testcaseInput[nCase][nIndex])
			{
				testcaseOutput[nIndex] = ' ';
			}
			else
			{
				testcaseOutput[nIndex] = map[int(testcaseInput[nCase][nIndex] - 'a')];
			}
		}
		testcaseOutput[strlen(testcaseInput[nCase])] = 0;
		printf("%s\n", testcaseOutput);
	}
	_getch();*/

	char map[27] = "yhesocvxduiglbkrztnwjpfmaq";
    /*char* testcaseInput = "3\nejp mysljylc kd kxveddknmc re jsicpdrysi\n"\
								"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"\
								"de kr kd eoya kw aej tysr re ujdr lkgc jv";*/
char* testcaseInput = /*"30\n"\
"ejp mysljylc kd kxveddknmc re jsicpdrysi\n"\
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"\
"de kr kd eoya kw aej tysr re ujdr lkgc jv\n"\
"hello i am the google code jam test data\n"\
"how are you\n"\
"aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee\n"\
"y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd\n"\
"schr rkxc tesr aej dksl tkrb xc\n"\
"tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd\n"\
"dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks\n"\
"w ew rte czjymd w ew esc czjymd esc\n"\
"wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte\n"\
"ys cac wep ys cac ysi y vklces wep y vklces\n"\
"eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq\n"\
"rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx\n"\
"tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd\n"\
"kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx\n"\
"wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc\n"\
"seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr\n"\
"na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd\n"\
"bet ypc aej bemiksl jv ncfyjdc kx y veryre\n"\
"eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr\n"\
"eb seeeee lellymep kd bcyici wep rbc epvbysylc\n"\
"eb xa lei mcrd xyoc ejr\n"\
"kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd\n"\
"wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso\n"\
"rbkd kd de chfkrksl k bygc re le rbc nyrbpeex\n"\
"ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi\n"\
"pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb\n"\
"vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd";*/

"30\n"\
"ejp mysljylc kd kxveddknmc re jsicpdrysi\n"\
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"\
"de kr kd eoya kw aej tysr re ujdr lkgc jv\n"\
"hello i am the google code jam test data\n"\
"how are you\n"\
"aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee\n"\
"y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd\n"\
"schr rkxc tesr aej dksl tkrb xc\n"\
"tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd\n"\
"mcr mkvd ie tbyr bysid ie\n"\
"kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd\n"\
"vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd\n"\
"eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq\n"\
"ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi\n"\
"ejp feic uyx kd mkoc rbc varbylepcys rbcepcx\n"\
"rbcpc kd se ysdtcp\n"\
"eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr\n"\
"set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd\n"\
"w ew rte czjymd w ew esc czjymd esc\n"\
"wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte\n"\
"lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd\n"\
"k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja\n"\
"cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc\n"\
"ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej\n"\
"na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd\n"\
"ys cac wep ys cac ysi y vklces wep y vklces\n"\
"dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks\n"\
"aej vkddci eww rbc fbkfocs myia\n"\
"ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd\n"\
"ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi\n";

	char testcaseOutput[3500] = "";
	memset(testcaseOutput, 0, 3500);
	char *inputData = strstr(testcaseInput, "\n");
//	char inputCount[4];
//	strncpy(inputCount, testcaseInput, inputData - testcaseInput);
//	inputCount[inputData - testcaseInput] = 0;
	inputData++;
//	char numCases = atoi(inputCount);
	char testcaseNum = 1;
	char casestring[20] = "";
	sprintf_s(casestring, 20, "Case #%d: ", testcaseNum++);
	strcat_s(testcaseOutput, 3500, casestring);
	for (unsigned int nIndex = 0; nIndex < strlen(inputData); nIndex++)
	{
		if ('a' > inputData[nIndex] || 'z' < inputData[nIndex])
		{
			if ('\n' == inputData[nIndex])
			{
				sprintf_s(casestring, 20, "\nCase #%d: ", testcaseNum++);
				strcat_s(&testcaseOutput[nIndex], 3500-nIndex, casestring);
			}
			else
			{
				strncat_s(&testcaseOutput[nIndex], 3500-nIndex, &inputData[nIndex], 1);
			}
		}
		else
		{
			strncat_s(&testcaseOutput[nIndex], 3500-nIndex, &map[int(inputData[nIndex] - 'a')], 1);
		}
	}
	printf("%s\n", testcaseOutput);

	_getch();

	return 0;
}

