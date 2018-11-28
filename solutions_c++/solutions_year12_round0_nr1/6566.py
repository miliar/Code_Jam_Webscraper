#include <cstdlib>
#include <iostream>

using namespace std;


void findDecodingMap( const char * code[], const char * decode[], int len , char decodingMap[] ) {
    const char * pC = NULL, * pD = NULL;
    
    for( int i=0; i<len; i++ ) {
        pC = &code[i][0];
        pD = &decode[i][0];
        while( *pC && *pD ) {
            if( *pD >= 'a' && *pD <= 'z' )
                decodingMap[*pC-'a'] = *pD;
            pC++;
            pD++;
        }
    }
}

void decoding( char input[], char decodingMap[] , int num ) {
    
    const char * src = input;
    char result[101];
    char * dst = result;
    
    while( *src ) {
        if( *src >= 'a' && *src <= 'z' )
            *dst = decodingMap[*src-'a'];
        else
            *dst = *src;
        dst++;
        src++;
    }
    
    *dst = 0;
    
    cout << "Case #" << (num+1) << ": " << result << endl;
    
}

/*
 * 
 */
int main(int argc, char** argv) {
    
    // sample for making decoding table
    
    const char * code[] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };
    
    const char * decode[] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    };
    
    char decodingMap[26];
    char lookForQ[26];
    
    // making decoding table
    
    
    for( int i=0; i<26; i++) {
        decodingMap[i] = '!';
        lookForQ[i] = 1;
    }
    
    decodingMap['q'-'a'] = 'z';
    
    findDecodingMap( code, decode, 3, decodingMap );
    
    for( int i=0; i<26; i++ ) {
        lookForQ[decodingMap[i]-'a'] = 0;
    }
    
    char q = 0;
    for( int i=0; i<26; i++ ) {
        if( lookForQ[i] )
            q = (char)(i+'a');
    }
    
    decodingMap['z'-'a'] = q;
    
    // decoding input
    
    int numInput = 0;
    char dummy;
    
    cin >> numInput; // read number of line
    cin.get(dummy);
    
    char inputMsg[102];
    
    for( int i=0; i < numInput; i++ ) {
        cin.getline( inputMsg, 101 );
        decoding( inputMsg, decodingMap, i );
    }

    return 0;
}

