#include <iostream.h>
#include <fstream.h>

#include <stdio.h>
#include <stdlib.h>




#define MAXLEN 1000

unsigned __int64 T, N, X, K;



unsigned __int64 closestnum;
unsigned __int64 readnum;


unsigned __int64 n;

char* pch;

unsigned __int64 count = 0;

 
char sLine[MAXLEN];

char currentletter;

ifstream inFile;

#define MAX_STACK_SIZE 1000

void Push(char n);
char Pop(void);
void PrintStack(void);
void InitializeData(unsigned n);
void FreeData(void);
char RemoveItem(unsigned pos);
void InsertItem(char n, unsigned pos);


static char stack[MAX_STACK_SIZE];
static int top = -1;

static unsigned size;


/*  Initialize memory for data  */

void InitializeData(unsigned n) {
    size = n;
}


/*  Free memory used for data  */

void FreeData(void) {
    return;
}


/*  Remove data item at position 'pos'  */

char RemoveItem(unsigned pos) {
    char d = sLine[pos];

    if ( pos >= size-- ) {
        fprintf(stderr, "Data position %u is out of bounds.\n", pos);
        exit(EXIT_FAILURE);
    }

    while ( pos < size ) {
        sLine[pos] = sLine[pos+1];
        ++pos;
    }

    return d;
}


/*  Insert data item 'n' at position 'pos'  */

void InsertItem(char n, unsigned pos) {
    int i = (signed) size;

    if ( pos > size++ ) {
        fprintf(stderr, "Data position %u is out of bounds.\n", pos);
        exit(EXIT_FAILURE);
    }

    while ( --i >= (signed) pos )
        sLine[i+1] = sLine[i];

    sLine[pos] = n;
}

/*  Push item 'n' onto the stack  */

void Push(char n) {
    if ( ++top == MAX_STACK_SIZE ) {
        fprintf(stderr, "Stack full!\n");
        exit(EXIT_FAILURE);
    }

    stack[top] = n;
}


/*  Pop top item from the stack  */

char Pop(void) {
    if ( top < 0 ) {
        fprintf(stderr, "Stack empty!\n");
        exit(EXIT_FAILURE);
    }

    return stack[top--];
}


/*  Output contents of stack  */

void PrintStack(void) {
    int i = 0;
	unsigned __int64 num;
	char cnum[1000];
	
    while ( i <= top )
	{
		cnum[i] = stack[i++];
        //putchar(stack[i++]);
	}
	cnum[i] = 0;
	num = atoi(cnum);
	
	//printf("%d\n",num);
	if ( num > readnum )
	{
		if ( closestnum == readnum )
		{
			closestnum = num;
		}
		else
		{
			if ( (closestnum - readnum) > (num-readnum) )
				closestnum = num;
		}
	}
	
    //putchar('\n');
}




void Perm(unsigned n) {
    unsigned item;

    if ( n == 0 ) {
        PrintStack();
        ++count;
        return;
    }

    for ( item = 0; item < n; ++item ) {
        Push(RemoveItem(item));
        Perm(n-1);
        InsertItem(Pop(), item);
    }
}

unsigned item;

int main(int argc, char* argv[])
{
	if ( argc < 2 )
	{
		inFile.open("B-test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	inFile.getline(sLine,MAXLEN);
	
	
	for (X=0;X<T;X++)
	{
		inFile.getline(sLine,MAXLEN);
		
		pch = &sLine[strlen(sLine)];
		closestnum = atoi(sLine);
		readnum = closestnum;
		*pch = '0';
		pch++;
		*pch = 0;
		n = strlen(sLine);
		
		InitializeData(n);
		
		
		Perm(n);
		
		/*
		printf("Permutations of %u items:\n\n", n);
		Perm(n);
		printf("\n%d permutations in all.\n", count);
		FreeData();
		*/
		
		
		
		
		
		
		
		
		cout << "Case #" << X+1 << ": " << closestnum << endl;

	}
	
	inFile.close();
	return 0;
}