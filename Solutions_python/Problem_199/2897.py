def flip_shit(file):
    input_list = file.readlines()
    cases = int(input_list[0])
    for i in range(1, cases + 1, 1):
        pancake_row = input_list[i].split()[0]
        size = int(input_list[i].split()[1])
        print('Case #' + str(i) + ': ' + str(check_flips(pancake_row, size)))
    
    
def check_flips(pancakes: str, size: int) -> str:
    original_row = pancakes
    flip_history = {original_row}
    flips = 0
    on_left = True
    
    while pancakes != '+' * len(original_row):
        flip_index = -1
        #find first - from the left
        if on_left:
            for char in range(len(pancakes)):
                if pancakes[char] == '-':
                    flip_index = char
                    break
            if flip_index == -1:
                on_left = False
            else:
                pancakes = flipped_some(pancakes, size, flip_index, on_left)
                on_left = False
        else:
        # find first - from the right
            for char in range(len(pancakes) - 1, -1, -1):
                if pancakes[char] == '-':
                    flip_index = char
                    break
            if flip_index == -1:
                on_left = True
            else:
                pancakes = flipped_some(pancakes, size, flip_index, on_left)
                on_left = True
        flips+=1
        if pancakes in flip_history:
            return 'IMPOSSIBLE'
        else:
            flip_history.add(pancakes)
        
    return flips
            
def flipped_some(to_flip:str, size: int, index: int, left: bool) -> str:
    if left:
        if index + size - 1 >= len(to_flip):
            return to_flip
        else:
            return_str = to_flip[:index]
            for i in range(index, index + size, 1):
                if to_flip[i] == '+':
                    return_str += '-'
                elif to_flip[i] == '-':
                    return_str += '+'
            return_str += to_flip[index + size:]
    else:
        if index - size + 1 <= 0:
            return to_flip
        else:
            return_str = to_flip[:index - size + 1]
            for i in range(index-size + 1, index + 1, 1):
                if to_flip[i] == '+':
                    return_str += '-'
                elif to_flip[i] == '-':
                    return_str += '+'
            return_str += to_flip[index + 1:]
    return return_str
        
flip_shit(open('A-large.in', 'r'))