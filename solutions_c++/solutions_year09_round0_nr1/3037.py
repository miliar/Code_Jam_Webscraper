#include <stdio.h>

class node {
public:
    char c;
    
    node * brother;
    
    node * son;
};

class list {
public:
    node * value;
    
    list * next;

};
int remove(node *);
int count1 = 0;
int main(int argc, char ** argv) {
    
    
    int wordCount;
    int wordCountIndex;
    int length;
    int lengthIndex;
    int caseCount;
    int caseIndex;
    
    scanf("%d %d %d",&length, &wordCount, &caseCount);
    
    node Root;
    Root.c = '\0';
    Root.brother = 0;
    Root.son = 0;
    for(wordCountIndex = 0; wordCountIndex < wordCount; wordCountIndex++) {
        char * word = new char[length];
        scanf("%s",word);
        //printf("%s \n",word);
        node * fatherOfCurrent = &Root;
        node * current = Root.son;
        node * previous = 0;

        for(lengthIndex = 0; lengthIndex < length; lengthIndex++) {
            char currentChar = word[lengthIndex];
            
            while(current != 0) {
                if(current->c == currentChar)
                {
                    //next = current;
                    
                    fatherOfCurrent = current;
                    current = current -> son;
                    break;
                }     
                previous = current;
                current = current -> brother;        
            }
            if(current == 0) {
                if(fatherOfCurrent -> son == 0) {
                    //printf("son of father is null");               
                    node* newNode = new node();
                    newNode -> c = currentChar;
                    newNode -> brother = 0;
                    newNode -> son = 0;
                    fatherOfCurrent->son = newNode;
                    
                    fatherOfCurrent = newNode;
                    current = newNode->son; 
                } else {
                    //printf("brother of the previous is null");   
                    node* newNode = new node();
                    newNode -> c = currentChar;
                    newNode -> brother = 0;
                    newNode -> son = 0;
                    previous -> brother = newNode;
                    
                    fatherOfCurrent = newNode;
                    current = newNode->son;
                }                   
            }
                       
        }
        delete[] word;
    }
    for(int caseIndex = 0; caseIndex < caseCount; caseIndex++) {
        char * caseWord =  new char[600];
        /*for(int x = 0; x < 600; x++)
            caseWord = '\0';*/
        scanf("%s \n",caseWord);
        //printf("%s \n",caseWord);
        int hasCase = 0;
        int flag = 0; int flagContinue = 1;

        list * list2Index = new list();
        list2Index -> value = &Root;
        list2Index -> next = 0;
        list * list2original = list2Index;
        list * list1Index = 0;
        list * index_list1Index = 0;
        int count_count = 0;
        for(int x = 0; x<600; x++) {
            if(caseWord[x] == '\0')
                break;
            
            if(flagContinue == 0) 
                break;
            switch(caseWord[x]) {
                case '(':
                   //printf("( \n");
                   flag = 1;
                   break;
                case ')':
                   //printf(") \n");
                   flag = 0;
                   if(list1Index == 0)
                       flagContinue = 0;
                   list2Index = list1Index;
                   list2original = list2Index;
                   list1Index = 0;
                   
                   count_count++;        
                   break;
                default:
                   list2Index = list2original;
                   while(list2Index  != 0) {
                      //printf("%d \n",count_count);
                      node* current1 =  list2Index  -> value -> son;
                      while(current1 != 0) {
                           if(caseWord[x] == current1 ->c) {
                               
                               //printf("%c \n", current1->c);
                               flagContinue = 1;
                               if(count_count == length - 1) {
                                    hasCase++;
                                    
                               }               
                               list * newNode = new list();
                               newNode-> value = current1;
                               newNode -> next = 0;
                               if(list1Index == 0) {
                                   list1Index = newNode;
                                   index_list1Index = list1Index;
                               } else {
                                   index_list1Index -> next = newNode;
                                   index_list1Index = newNode;
                               }                    
                            } 
                            current1 = current1 -> brother;              
                      }
                      list2Index = list2Index->next;
                      //printf("next next \n");                       
                   }
                   
                   if(flag == 0) {
                       if(list1Index == 0)
                           flagContinue = 0;    
                       list2Index = list1Index;
                       list2original = list2Index;
                       list1Index = 0;
                       count_count++;
                   }        
                   break;                        
            }
            
                                  
        }
        printf("Case #%d: %d \n", caseIndex+1, hasCase);            
        delete caseWord;    
    }
    
    return 0;
}

int remove(node * begin) {
   if(begin->son ==0 && begin->brother == 0) {
        delete begin;
        count1++;
        return 1;
   }  else if(begin->son !=0&&begin->brother !=0) {
       //printf("remove left & right child \n");
       if(remove(begin->son)==1 && remove(begin->brother)==1) {
           delete begin;
           
           count1++;
           
           return 1;
       }
           
   }else if(begin -> son !=0) {
      //printf("remove left child \n");
      if(remove(begin->son)==1)
      {
          delete begin;
          count1++;
          
          return 1;
      }
   }  
   else if(begin->brother !=0) {
         //printf("remove right child\n");
        if(remove(begin->brother)==1)
        {
            
            delete begin;
            count1++;
           
            return 1;
        }
   }                          
}
