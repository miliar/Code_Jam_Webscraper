// google code jam 001.cpp : メイン プロジェクト ファイルです。

#include "stdafx.h"
#include <cstdio>
#include <cstring>

using namespace System;
const int length = 100;

int main(array<System::String ^> ^args)
{
    printf("%d", 'z'-'a');

    char input[3][length] =
    {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
      "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

    char output[3][length] =
        {"our language is impossible to understand",
         "there are twenty six factorial possibilities",
         "so it is okay if you want to just give up"};

    char input2[30][102] = 
{"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"hello i am the google code jam test data",
"how are you",
"aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee",
"y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd",
"schr rkxc tesr aej dksl tkrb xc",
"wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso",
"w ew rte czjymd w ew esc czjymd esc",
"wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte",
"pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb",
"k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja",
"set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd",
"na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd",
"cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc",
"ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej",
"ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi",
"kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx",
"wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc",
"seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr",
"tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd",
"mcr mkvd ie tbyr bysid ie",
"rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx",
"aej tysr dcmm rbksld yr xc neksl qeeex",
"ys cac wep ys cac ysi y vklces wep y vklces",
"vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd",
"lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd",
"eb seeeee lellymep kd bcyici wep rbc epvbysylc",
"eb xa lei mcrd xyoc ejr"};




    char inmapping[26] = {0};
    char mapping[26] = {0};
    int flag[26] = {0};
    for(int i=0;i<26;i++){
        flag[i] = 0;
    }

    int count = 0;
    for(int i=0;i<3;i++){
        for(int j=0;j<300;j++){
            if(input[i][j] != ' '){
                if(flag[input[i][j]-'a'] == 1){
                    continue;
                }
                inmapping[output[i][j]-'a'] = input[i][j];
                mapping[input[i][j]-'a'] = output[i][j];
                flag[input[i][j]-'a'] = 1;
                count++;
                printf("[%d][%d] --> [%d] %d\n", i, j, (int)input[i][j], count);
                if(count >= 26){
                    break;
                }
            }
        }
    }
    for(int i=0;i<26;i++){
        printf("%d", flag[i]);
        if(flag[i] == 0){
            mapping['z'-'a'] = 'q';
            mapping['q' - 'a'] = 'z';
        }
    }
    printf("\n");
    for(int i=0;i<26;i++){
        printf("%c", 'a'+i);
    }
    printf("\n");
    for(int i=0;i<26;i++){
        printf("%c", mapping[i]);
    }
    printf("\n");


    FILE *fp;
    if ((fp = fopen("output.txt", "w")) == NULL) {
        printf("file open error!!\n");
        return -1;
    }
    for(int i=0;i<30;i++){
        printf("Case #%d: ", i);
        fprintf(fp, "Case #%d: ", i+1);
        for(int j=0;j<102-1;j++){
            if(input2[i][j] != ' '){
                printf("%c", mapping[input2[i][j]-'a']);
                fputc(mapping[input2[i][j]-'a'], fp);
            }else{
                printf(" ");
                fputs(" ", fp);
            }
        }
        fprintf(fp, "\n");
        printf("\n");
    }

    int dummy;
    scanf("%d",dummy);
    return 0;
}
