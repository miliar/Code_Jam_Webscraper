#include<cstdio>



char *create_mapping_table(){
  char *str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  char *str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  char *str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

  char *o_str1= "our language is impossible to understand";
  char *o_str2 = "there are twenty six factorial possibilities";
  char *o_str3 = "so it is okay if you want to just give up";

  char *array = new char[26];//mapping from cipher to plain text

  char *temp_1 , *temp_2;
  int i=0;

  temp_1 = str1; temp_2 = o_str1;
   

  for(i=0; i<26; i++)array[i]=0;

  i = 0;
  while(*temp_1){
    if(*temp_1 == ' '){
      temp_1++; temp_2++;
      continue;
    }
    array[*temp_1 - 'a'] = *temp_2;
        temp_1++; temp_2++;
 }

 temp_1 = str2; temp_2 = o_str2;

  while(*temp_1){
    if(*temp_1 == ' '){
      temp_1++; temp_2++;
      continue;
    }
    array[*temp_1 - 'a'] = *temp_2;
    temp_1++; temp_2++;
 }

 temp_1 = str3; temp_2 = o_str3;

 while(*temp_1){
    if(*temp_1 == ' ') {
      temp_1++; temp_2++;
      continue;
    }
    array[*temp_1 - 'a'] = *temp_2;
    temp_1++; temp_2++;
 }

 array['q'-'a'] = 'z';
 array['z'-'a'] = 'q';

 /*for(i=0; i<26; i++){
   if(array[i]==0){
     printf("%c\n", 'a'+i);
   } else {
     printf("%c : %c \n", array[i], 'a'+i);
   }
 }*/
 return array;
}

void decrypt()
{
  char str[105];
  char *map_array = create_mapping_table();
  int n,i;

  scanf("%d", &n);
  fgetc(stdin);
  for(i=0;i<n;i++){
    fgets(str, 105, stdin);
    printf("Case #%d: ", i+1);
    int j=0;
    while(str[j]){
      if(str[j]==' ' || str[j]=='\n'){
        printf("%c",str[j]);j++;
      } else {
        printf("%c", map_array[str[j]-'a']);
        j++;
      }
    }
  }
  delete map_array;
}


int main(){

  decrypt();
  return 0;
}

