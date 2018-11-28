#include <stdio.h>
#include <stdlib.h>

struct node
{
    int key;
    struct node *next;
};

////in this file////////
int addBegin(struct node ** head , int newElement);
int addEnd(struct node **head, int newElement);
int remBegin(struct node **head, int *val);
int remEnd(struct node **head, int *val);
void printList(struct node *head);
int lengthList(struct node *head);

int searchList( struct node *head, int val);
////////end of prototypes////////


//searches the list, returns
//1 --> found
//-1 --> not found
int searchList( struct node *head, int val)
{
    while( head != NULL )
    {
	if( head->key == val )    //found
	    return 1;
	head=head->next;
    }
    return -1;
}


//returns length of the list
int lengthList(struct node *head)
{
    int count=0;
    while( head != NULL )
    {
	count++;
	head=head->next;
    }

    return count;
}



//returns 0 on success, 1 on fail
int addBegin(struct node ** head , int newElement)
{
    if(*head == NULL)
    {
	*head = (node * )malloc(sizeof(struct node));
	(*head)->key=newElement;
	(*head)->next=NULL;
	return 0;
    }

    struct node * tmp = (node *)malloc(sizeof(struct node)) ;
    tmp->key = newElement;
    tmp->next = *head;
    *head = tmp;
    return 0;
}


int addEnd(struct node **head, int newElement)
{
    if(*head == NULL)
    {
	*head = (node *)malloc(sizeof(struct node));
	(*head)->key=newElement;
	(*head)->next=NULL;
	return 0;
    }
    
    struct node * end=*head;
    while(end->next != NULL)
    {
	end = end->next;
    }

    struct node * newNode = (node *)malloc(sizeof(struct node)) ;
    newNode->next = NULL;
    newNode->key = newElement;

    end->next = newNode;
    return 0;
}

//remove node from begin,
//return 0 on success, 1 on fail
//store the result in val
int remBegin(struct node **head, int *val)
{
    if(*head == NULL)
    {
	//no more elements
	*val=0; //setting zero, dont use this val, incase returns 1
	return 1;
    }

    if((*head)->next == NULL)
    {
	*val= (*head)->key;
	free(*head);
	*head=NULL;
	return 0;
    }

    struct node * toReturn = *head;
    *head = (*head)->next;
    toReturn->next=NULL;
    
    *val = toReturn->key;
    free(toReturn);
    return 0;
}


//remove from end
//returns 0 on success, 1 on fail
//store result in *val
int remEnd(struct node **head, int *val)
{
    if(*head == NULL)
    {
	//no more elements
	*val=0;
	return 1;
    }

    if((*head)->next == NULL)
    {
	*val= (*head)->key;
	free(*head);
	*head=NULL;
	return 0;
    }

    struct node *endNode = *head;
    while(endNode->next->next != NULL)
    {
	endNode= endNode->next;
    }
    *val = endNode->next->key;
    free(endNode->next);
    endNode->next=NULL;
    return 0;
}
    
    
void printList(struct node *head)
{
    //puts("________________________________________________________________________________");
    while(head != NULL)
    {
	printf("%c | ",head->key);
	head = head->next;
    }
    //puts(" |");
    
    //puts("NULL");
    //puts("________________________________________________________________________________");
}
    
    
    

struct StData
{
    node ** heads;
    char * regx_str;
};


//note that SD is passed by ref, and is not that array is passed
void eval_regx( char ** dict, StData * SD, int D )
{
    int count=0;

    for( int d=0; d<D; d++ )    //for each word in dict
    {
	int i;
	for( i=0 ; dict[d][i] != 0 ; i++ )  //for a particular string in dict, going thru each char
	{
	    if( SD[0].regx_str[i] == '_' ) //wildcard
	    {
		if( searchList( SD[0].heads[i], dict[d][i] ) == 1 ) //could find a match
		{
		    continue;
		}
		else
		{
		    break;
		}
	    }

	    if( (dict[d][i] == SD[0].regx_str[i])  &&  (SD[0].regx_str[i] != '_') ) //matches.
	    {
		continue;
	    }

	    if( (dict[d][i] != SD[0].regx_str[i])  &&  (SD[0].regx_str[i] != '_') ) //doesnot match.
	    {
		break;
	    }
	}
	if( dict[d][i] == 0 )
	    count++;
    }
    //printf("occurences found=%d\n", count);
    printf("%d", count);
}

    



node ** make_stack( char * str, int L )
{
    //array of stacks
    node ** h= (node ** ) malloc( (50) * sizeof(node *) );
    for(int i=0;i<50;i++) h[i]=NULL;


    int k=0; //indexing of stacks
    for(int i=0 ; str[i] != 0 ; i++ )
    {
	if( str[i] == '(' )
	{
	    i++;
	    while( str[i] != ')' )
	    {
		addBegin( &h[k], str[i] );
		i++;
	    }
	    k++;
	}
	else
	{
	    addBegin( &h[k], str[i] );
	    k++;
	}
    }
    return h;
}

void fix_constant( node ** heads, char * str_new )
{
    int i;
    for( i=0 ; heads[i] != NULL ; i++ )
    {
	if( lengthList( heads[i] )  ==  1 )
	{
	    str_new[i]=heads[i]->key;
	}
	else
	{
	    str_new[i]='_';
	}
    }
    str_new[i]=0;
}




int main()
{
    int L,D,N;
    scanf("%d %d %d\n", &L, &D, &N);

    //sample gets ... not req.
    //gets(a);

    //memory allocate for storing all words in dictionary
    char ** all_words = (char ** )malloc( (D+3) * sizeof(char*) );
    for(int i=0 ; i<D ; i++ )
    {
        all_words[i]=(char*)malloc( (L+5) * sizeof(char) );
    }


    //input the dict
    for( int i=0 ; i<D ; i++ )
    {
        gets(all_words[i]);
    }


    //array of all test-case bin-data
    StData * SD = ( StData * )malloc( N * sizeof( StData ) );


    //tmp str for storing test-case
    char a[1000];
    //input all test cases
    for( int i=0 ; i<N ; i++ )
    {
	gets( a );
	SD[i].heads = make_stack( a , L);
	SD[i].regx_str = (char *) malloc( 50 * sizeof(char) );

	fix_constant( SD[i].heads, SD[i].regx_str );
    }
    //now SD is ready to be used, sizeof SD is N


    ////sample.......not req
    //for( int i=0 ; i<N ; i++ )
    //{
    //    puts("____________________");
    //    puts( SD[i].regx_str);
    //    for(int  k=0 ; SD[i].heads[k] != NULL ; k++ )
    //    {
    //        printf(" %d :::",k);
    //        printList(SD[i].heads[k]);
    //        printf("\n");
    //    }
    //    puts("____________________");

    //}

    for( int r=0; r<N; r++ ) //for all regx
    {
	printf("Case #%d: ", r+1);
	eval_regx( all_words, &SD[r], D ); //passing first regx just for sample
	printf("\n");
    }



    //making stacks and the wild string
    //sample... not req.
    //node ** heads=make_stack( a );
    //fix_constant( heads, resultant);

    //for( int i=0; heads[i]!=NULL; i++ )
    //{
    //    printf(" %d :::",i);
    //    printList(heads[i]);
    //    printf("\n");
    //}

    //puts( resultant );
}
