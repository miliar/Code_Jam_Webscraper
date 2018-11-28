#include <cstdio>
#include <cstring>

const char INPUT_NAME[] = "A-Large.in";
const char OUTPUT_NAME[] = "A-Small.out";
const int BUFFER_LENGTH = 600;

int possibleMatch(char* string, char* dictString){
    char* chPtr = string;
    int match = true;
    int strLength = strlen(dictString);
    for (int i=0; match && i<strLength; i++){
        match = false;
        if (*chPtr == '('){
            while (*chPtr != ')'){
                if (*chPtr == dictString[i]){
                    match = true;
                }
                chPtr++;
            }
            chPtr++;
        } else if (*chPtr == dictString[i]){
            match = true;
            chPtr++;
        } else{
            match = false;
        }
    }
    return match;
}

int main(){
    FILE* input = fopen(INPUT_NAME, "r");
    FILE* output= fopen(OUTPUT_NAME, "w");
    int dictSize;
    int stringLength;
    int numTests;
    char** dictionary = NULL;
    char buffer[BUFFER_LENGTH]; 
    if (input != NULL){
        fscanf(input, "%d %d %d\n", &stringLength, &dictSize, &numTests);
        dictionary = new char*[dictSize];
        for (int i=0; i<dictSize; i++){
            //One for null byte
            dictionary[i] = new char[stringLength + 1];
            fgets(buffer, BUFFER_LENGTH, input);
            strncpy(dictionary[i], buffer, stringLength);
            dictionary[i][stringLength] = '\0';
        }
        
        for (int i=0; i<numTests; i++){
            int count = 0;
            fgets(buffer, BUFFER_LENGTH, input);

            for (int j=0; j<dictSize; j++){
                count += possibleMatch(buffer , dictionary[j]);
            }
            fprintf(output, "Case #%d: %d\n", i+1, count);
        }
        for (int i=0; i<dictSize; i++){
            delete[] dictionary[i];
        }
        fclose(input);
    }
}
