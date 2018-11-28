#include <iostream>

using namespace std; 	//introduces namespace std


template <class T>
class List
{
	public:
		T *root;
		unsigned long num;
		List();
		~List();
		void 	Clear();
		T		*New();
		void 	Delete(T *sprite);
		bool    Delete(unsigned long n);
		T       *Get(unsigned long n);
};

//CONSTRUCTOR
template <class T>
List<T>::List()
{
	root=new T;
	root->prev=NULL;
	root->next=NULL;
	num=0;
}
//DESTRUCTOR
template <class T>
List<T>::~List()
{
	Clear();
	if(root!=NULL)delete root;
	root=NULL;
}
//CLEAR
template <class T>
void List<T>::Clear()
{
	if(root!=NULL)
	{
		T *temp=NULL,*CurrentPtr = root->next;
		while(CurrentPtr != NULL)
		{
			temp=CurrentPtr;
			CurrentPtr = CurrentPtr->next;
			delete temp;
		}
		root->next=NULL;
	}
	num=0;
}
//NEW
template <class T>
T *List<T>::New()
{
	T *temp;
	temp=new T;
	temp->prev=root;
	temp->next=root->next;
	//
	if(root->next!=NULL)root->next->prev=temp;
	root->next=temp;
	//
	num++;
	
	return temp;
}
//DELETE
template <class T>
void List<T>::Delete(T *sprite)
{
	if(!sprite)return;
	if(sprite!=root)//protect the root from being deleted
	{
		sprite->prev->next=sprite->next;
		if(sprite->next!=NULL)sprite->next->prev=sprite->prev;
		delete sprite;
		sprite=NULL;
		num--;
	}
}
template <class T>
bool List<T>::Delete(unsigned long n)
{
	T *temp=Get(n);
	if(temp)
	{
		Delete(temp);
		return true;
	}
	return false;
}
//GET
template <class T>
T *List<T>::Get(unsigned long n)
{
	if(root!=NULL)
	{
		T *CurrentPtr = root->next;
		unsigned long i=0;
		while(CurrentPtr != NULL)
		{
			if(i==n)return CurrentPtr;
			i++;
			CurrentPtr = CurrentPtr->next;
		}
	}
	return NULL;
}

////////////////////////////

#define NUM_WORDS	5000

class Word
{
	public:
		char str[1024];
};

class Character
{
	public:
		char c;
		Character *prev,*next;
};

class Characters
{
	public:
		int length;
		List <Character> chars;
		Characters *prev,*next;
		void Add(char c)
		{
			Character *s = chars.New();
			if(s)
			{
				s->c = c;
			}
		}
		bool HasCharacter(char c)
		{
			Character *s = chars.root->next;
			while(s)
			{
				if(s->c == c)
					return true;
				s = s->next;
			}
			return false;
		}
};

class Blurb
{
	public:
		List <Characters> digit;
		bool HasString(char *str)
		{
			for(int i=0;i<strlen(str);i++)
			{
				Characters *C = digit.Get(digit.num-1-i);
				if(!C->HasCharacter(str[i]))
				{
					return false;
				}
			}
			//printf("%s has %s\n",Print(),str);
			return true;
		}
		void MakeFromString(char *str)
		{
			Characters *chars = NULL;
			int d = 0;
			bool started = false;
			for(int i=0;i<strlen(str);i++)
			{
				if(str[i]=='(')
				{
					chars = digit.New();
					started = true;
				}else
				if(str[i]==')')
				{
					started = false;
				}else
				if((str[i]>='a')and(str[i]<='z'))
				{
					if(!started)
					{
						chars = digit.New();
					}
					chars->Add(str[i]);
				}
			}
		}
		char print_str[1024];
		char *Print()
		{
			sprintf(print_str,"\0");
			Characters *C = digit.root->next;
			for(int i=0;i<digit.num;i++)
			{
				Characters *C = digit.Get(digit.num-1-i);
				if(C)
				{
					Character *s = C->chars.root->next;
					while(s)
					{
						sprintf(print_str,"%s%c,",print_str,s->c);
						s = s->next;
					}
					sprintf(print_str,"%s-\n",print_str);
				}
			}
			return print_str;
		}
};

class Dictionary
{
	public:
		long L,D,N;
		Word word[NUM_WORDS];
		Blurb blurb[NUM_WORDS];
		Dictionary()
		{
			L = 0;
			D = 0;
			N = 0;
		}
		void Load(char *fname)
		{
			FILE *file = fopen(fname,"rb");
			if(file)
			{
				char str[1024];
				fgets(str,1024,file);
				sscanf(str,"%d %d %d",&L,&D,&N);
				printf("%d,%d,%d\n",L,D,N);
				//read in dictionary
				printf("\nDictionary:\n");
				for(int i=0;i<D;i++)
				{
					char temp[1024];
					sprintf(word[i].str,"\0");
					fgets(temp,1024,file);
					for(int ii=0;ii<strlen(temp);ii++)
					{
						if((temp[ii]=='(')or(temp[ii]==')')
						 or((temp[ii]>='a')and(temp[ii]<='z')))
						 {
						 	sprintf(word[i].str,"%s%c",word[i].str,temp[ii]);
						 }
					}
					//printf("	%s\n",word[i].str);
				}
				//now read in test cases
				printf("\nTests:\n");
				for(int i=0;i<N;i++)
				{
					char str[1024];
					fgets(str,1024,file);
					blurb[i].MakeFromString(str);
					//printf("	%s*****\n%s",str,blurb[i].Print());
				}
				fclose(file);
			}
		}
		void GetMatches()
		{
			FILE *file = fopen("output.txt","wb");
			if(file)
			{
				for(int i=0;i<N;i++)
				{
					int matches = 0;
					for(int ii=0;ii<D;ii++)
					{
						if(blurb[i].HasString(word[ii].str))
						{
							matches++;
						}
					}
					char str[1024];
					sprintf(str,"Case #%d: %d\n",i+1,matches);
					fwrite(str,sizeof(char)*strlen(str),1,file);
				}
				fclose(file);
			}
		}
}Dictionary;


int main( void )
{
	Dictionary.Load("input.in");
	Dictionary.GetMatches();
	return 0;
}