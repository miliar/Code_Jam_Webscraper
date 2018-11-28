// STL
#ifndef NDEBUG
	#include <iostream>
#endif
#include <string>
// C Libs
#include <cstdio>
#include <cstdlib>

/*
 * --------------------------------------------------
 *  GLOBAL VARS
 * --------------------------------------------------
 */
const std::size_t BOARD_SIZE = 4;
const std::size_t ROW_SIZE = BOARD_SIZE + 1;
const std::size_t COL_SIZE = BOARD_SIZE + 1;

enum StateTypeEnum {
	XWon,
	OWon,
	Draw,
	UComplete
};//enum StateTypeEnum

void
get_board_from_input(FILE * const __stream, char * __board_buffer);

StateTypeEnum
process_board(const char * __board_buffer);


int main()
{
	/*
	 * --------------------------------------------------
	 *  INIT
	 * --------------------------------------------------
	 */
#ifdef DEBUG
	FILE * const INPUT = fopen("file.in", "r");
#else
	FILE * const INPUT = stdin;
#endif// DEBUG
	char *__board_buffer =
		(char *)malloc(ROW_SIZE * COL_SIZE);

	std::size_t __case_size = 0;
	fscanf(INPUT, "%lu", &__case_size);

	/*
	 *--------------------------------------------------
	 * MAIN LOGIC
	 *--------------------------------------------------
	 */
	for(std::size_t __case_iter = 1lu; __case_iter <= __case_size; ++__case_iter) {
		get_board_from_input(INPUT, __board_buffer);

		StateTypeEnum __state = process_board(__board_buffer);
		fgetc(INPUT);

		switch(__state) {
			case XWon:
				fprintf(stdout, "Case #%lu: X won\n", __case_iter);
				break;
			case OWon:
				fprintf(stdout, "Case #%lu: O won\n", __case_iter);
				break;
			case Draw:
				fprintf(stdout, "Case #%lu: Draw\n", __case_iter);
				break;
			case UComplete:
				fprintf(stdout, "Case #%lu: Game has not completed\n", __case_iter);
				break;
			default:
				fputs("Error!", stdout);
		}//switch(__state)
	}//outer loop

	/*
	 *--------------------------------------------------
	 *CLEAN UP
	 *--------------------------------------------------
	 */
	free(__board_buffer);
#ifdef DEBUG
	fclose(INPUT);
#endif//DEBUG
}//main

void
get_board_from_input(FILE * const __stream, char * __board_buffer) {
	for(std::size_t __row = 0ul; __row < BOARD_SIZE; ++__row)
		fscanf(__stream, "%s", __board_buffer + COL_SIZE * __row);
}//get_board_from_input(__stream, __board_buffer)

StateTypeEnum
process_board(const char * __board_buffer) {
	bool __complete = true;

	// Check ROWs
	for(std::size_t __row = 0ul; __row < BOARD_SIZE; ++__row) {
		// get board[row][0]
		char __first_char = *(__board_buffer + COL_SIZE * __row + 0);
		if(__first_char == '.') {
			__complete = false;
			continue;
		}//if

		bool __a_row_of_4 = true;
		for(std::size_t __col = 1ul; __col < BOARD_SIZE; ++__col) {
			// get board[row][col]
			char __cur_char = *(__board_buffer + COL_SIZE * __row + __col);

			if(__cur_char != __first_char && __cur_char != 'T')
				__a_row_of_4 = false;
			if(__cur_char == '.') {
				__complete = false;
				break;
			}//if
		}//for
		
		if(__a_row_of_4 == true) {
			switch(__first_char) {
				case 'X':
					return XWon;
				case 'O':
					return OWon;
			}//switch(__first_char)
		}//if
	}//for--Check ROWs

	// Check Cols
	for(std::size_t __col = 0ul; __col < BOARD_SIZE; ++__col) {
		// get board[row][0]
		char __first_char = *(__board_buffer + __col);
		if(__first_char == '.') {
			__complete = false;
			continue;
		}//if

		bool __a_col_of_4 = true;
		for(std::size_t __row = 1ul; __row < BOARD_SIZE; ++__row) {
			// get board[row][col]
			char __cur_char = *(__board_buffer + COL_SIZE * __row + __col);

			if(__cur_char != __first_char && __cur_char != 'T')
				__a_col_of_4 = false;
			if(__cur_char == '.') {
				__complete = false;
				break;
			}//if
		}//for

		if(__a_col_of_4 == true) {
			switch(__first_char) {
				case 'X':
					return XWon;
				case 'O':
					return OWon;
			}//switch(__first_char)
		}//if
	}//for--Check Cols

	{ // Check Diags1
	bool __a_diag_of_4 = true;
	char __first_char = *(__board_buffer);
	for(std::size_t __diag_iter = 1ul;
			__diag_iter < BOARD_SIZE;
			++__diag_iter)
	{
		char __cur_char =
			*(__board_buffer + COL_SIZE * __diag_iter + __diag_iter);
		if(__cur_char != __first_char && __cur_char != 'T')
			__a_diag_of_4 = false;
		if(__cur_char == '.') {
			__complete = false;
			break;
		}//if
	}//for

	if(__a_diag_of_4 == true) {
		switch(__first_char) {
			case 'X':
				return XWon;
			case 'O':
				return OWon;
		}//switch(__first_char)
	}//if
	}//Check Diags1

	{ // Check Diags2
	bool __a_diag_of_4 = true;
	char __first_char = *(__board_buffer + BOARD_SIZE - 1);
	for(std::size_t __diag_iter = 1ul;
			__diag_iter < BOARD_SIZE;
			++__diag_iter)
	{
		char __cur_char = *(__board_buffer + COL_SIZE * __diag_iter + BOARD_SIZE-1-__diag_iter);
		
		if(__cur_char != __first_char && __cur_char != 'T')
			__a_diag_of_4 = false;
	}//for
	
	if(__a_diag_of_4 == true) {
		switch(__first_char) {
			case 'X':
				return XWon;
			case 'O':
				return OWon;
		}//switch(__first_char)
	}//if
	}//Check Diags2

	if(__complete == false)
		return UComplete;
	return Draw;
}//process_board(__board_buffer)

