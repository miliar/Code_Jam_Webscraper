#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <map>
//#include <numeric>
//#include <queue>
//#include <set>
//#include <string>
//#include <utility>
//#include <vector>

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (100)
#define N_MAX   (10)

//#define T_MAX   (2000)
//#define N_MAX   (1000000000000000)


int main(void) {
	  char line[1024];
    uint32 T;
	
    //scanf("%d", &T);
    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &T);
    //printf("T = %d\n", T);
	
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
   	    int i;
	    	char str[1024];
	    	char out[128];

        /* Test Case run once */
		    fgets(str, sizeof(str), stdin);

        memset(out, 0, sizeof(out));
        for (i=0; i<=strlen(str); i++)
        {
	        	switch (str[i])
  	      	{
  	      	case 'y': out[i] = 'a';	break;
  	      	case 'n': out[i] = 'b';	break;
  	      	case 'f': out[i] = 'c';	break;
  	      	case 'i': out[i] = 'd';	break;
  	      	case 'c': out[i] = 'e';	break;
  	      	case 'w': out[i] = 'f';	break;
            case 'l': out[i] = 'g';	break;
            case 'b': out[i] = 'h';	break;
            case 'k': out[i] = 'i';	break;
            case 'u': out[i] = 'j';	break;
            case 'o': out[i] = 'k';	break;
            case 'm': out[i] = 'l';	break;
            case 'x': out[i] = 'm';	break;
            case 's': out[i] = 'n';	break;
  	        case 'e': out[i] = 'o';	break;
  	        case 'v': out[i] = 'p';	break;
  	        case 'z': out[i] = 'q';	break;
  	        case 'p': out[i] = 'r';	break;
  	        case 'd': out[i] = 's';	break;
  	        case 'r': out[i] = 't';	break;
  	        case 'j': out[i] = 'u';	break;
            case 'g': out[i] = 'v';	break;
            case 't': out[i] = 'w';	break;
            case 'h': out[i] = 'x';	break;
            case 'a': out[i] = 'y';	break;
  	        case 'q': out[i] = 'z';	break;
  	        default:
	        	out[i] = str[i];
  	        	break;
  	        }
        }

        /* Print */
        printf("Case #%d: %s", Ti, out);
    }

    return 0;
}


